## app.R ##
library(shiny)
library(shinydashboard)
library(ggplot2)
library(net.security)

ui <- dashboardPage(
  skin = "red",
  dashboardHeader(title = "Shuriken dashboard"),
  dashboardSidebar(
    
    sidebarMenu(
      menuItem("Resum", tabName = "resum", icon = icon("thermometer-half")),
      menuItem("Nikto", tabName = "webvul", icon = icon("free-code-camp")),
      menuItem("Nmap", tabName = "webnmap", icon = icon("eye")),
      menuItem("SearchVuls", tabName = "search", icon = icon("bolt"))
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
              fluidRow(
                column(width = 12,
                    box (
                      dataTableOutput("webvul")
                    )
                )
              )
            
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
              fluidRow(
                column(width = 12,
                       box (
                         dataTableOutput("nmapvul")
                       )
                )
              )
              
      ),
      
      # Second tab content
      tabItem(tabName = "search",
              box(
                title="Insert CVE"
              )
      )
    )
  )
)

server <- function(input, output, session) { 
  
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
  
}

shinyApp(ui, server)
