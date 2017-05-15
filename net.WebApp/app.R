## app.R ##
library(shiny)
library(shinydashboard)
library(ggplot2)
library(net.security)
library(rworldmap)

ui <- dashboardPage(
  skin = "red",
  dashboardHeader(title = "Net.WebApp"),
  dashboardSidebar(
    
    sidebarMenu(
      menuItem("Resum", tabName = "resum", icon = icon("thermometer-half")),
      menuItem("Nikto", tabName = "webvul", icon = icon("free-code-camp")),
      menuItem("Nmap", tabName = "webnmap", icon = icon("eye")),
      menuItem("GeoIP", tabName = "geoip", icon = icon("bar-chart")),
      menuItem("SearchCVES", tabName = "searchVuls", icon = icon("bolt"))
    )
    
  ),
  dashboardBody(
    tabItems(
      # First tab content
      tabItem(tabName = "resum",
              fluidRow(
                box(plotOutput("numverofvuls", height = 1000),
                    width = 12)
              )  
      ),
      
      # Second tab content
      tabItem(tabName = "webvul",
              fluidRow(
                column(width = 12,
                  box(
                    title="Look for the vulnerabilities of a particular web extract from nikto",
                    textInput("urlVul", "Insert Url:"),
                    actionButton("webbutton", "Search")
                  )
                )
              ),
              dataTableOutput("webvul")
            
            
      ),
      
      # Second tab content
      tabItem(tabName = "webnmap",
              fluidRow(
                column(width = 12,
                       box(
                         title="Look for the vulnerabilities of a particular web extract from nmap",
                         textInput("urlVulnmap", "Insert Url:"),
                         actionButton("nmapbutton", "Search")
                       )
                )
              ),
              dataTableOutput("nmapvul")
              
      ),
      
      # Second tab content
      tabItem(tabName = "geoip",
              fluidRow(
                box(plotOutput("geo_IPmap", height = 1000),
                    width = 12)
              )  
              
      ),
      
      # Second tab content
      tabItem(tabName = "searchVuls",
              fluidRow(
                column(width = 12,
                       box(
                         selectInput("selectTipe", label = h3("Search CVEs by type: "), 
                                     choices = list("XSS" = 1, "SQL" = 2, "Authentication" = 3, "CSRF" = 4, "BufferOverFlow" = 5, "None"=6), 
                                     selected = 6)
                       )
                )
              ),
              dataTableOutput("cvesSearch")
              
      )
    )
  )
)

server <- function(input, output, session) {

  source("R/config_enviroment.R")
  
  t_wVuls <- GetNumberOfVuls()
  
  #Web vulneraviliti Nikto
  observeEvent(input$webbutton, {
    webvulsDataframe <- GetVulneravilityNikto_fromUrlDataframe(input$urlVul)
    output$webvul = renderDataTable({
      webvulsDataframe
    })
  })
  
  #Web vulneravility from nmap
  observeEvent(input$nmapbutton, {
    nmapvulsDataframe <- GetVulsNMAP_fromUrlDataframe(input$urlVulnmap)
    output$nmapvul = renderDataTable({
      nmapvulsDataframe
    })
  })
  
  #Number of vuls per web
  output$numverofvuls <- renderPlot({
   df2=t_wVuls[order(t_wVuls$Vulneravilitys),]
   df2$url=factor(df2$url,levels=df2$url)
   g <- ggplot(df2,aes(x=factor(url),y=Vulneravilitys)) + geom_bar(stat='identity') + coord_flip() + labs(y='Vulnerailitys',x='url')
   g + ggtitle("Number of vulnerabilities per scanned url") 
  })
  
  #GeoIP Map
  output$geo_IPmap <- renderPlot({
    n <- joinCountryData2Map(geoIP, joinCode="NAME", nameJoinColumn="country_name")
    newmap <- mapCountryData(mapTitle="World")
    newmap
    points(geoIP$longitude, geoIP$latitude, col = "red", cex = .6)
    })
  
  #Search CVEs
  #output$value <- renderPrint({ input$select })
  observeEvent(input$selectTipe, {
    if (input$selectTipe == 1)
    {
      CVEs_Dataframe <- Get_XSS_CVEs(1)
    }
    else if (input$selectTipe == 2)
    {
      CVEs_Dataframe <- Get_SQL_CVEs(1)
    }
    else if (input$selectTipe == 3)
    {
      CVEs_Dataframe <- Get_Auth_CVEs(1)
    }
    else if (input$selectTipe == 4)
    {
      CVEs_Dataframe <- Get_CSRF_CVEs(1)
    }
    else if (input$selectTipe == 5)
    {
      CVEs_Dataframe <- Get_BufferOverFlow_CVEs(1)
    }
    else
    {
      CVEs_Dataframe <- NULL
    }
    
    output$cvesSearch = renderDataTable(
      CVEs_Dataframe,
      options = list(scrollX = TRUE)
    )
  })
  
}

shinyApp(ui, server)
