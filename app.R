## app.R ##
library(shiny)
library(shinydashboard)
library(ggplot2)
library(net.security)
library(leaflet)
library(XML)

ui <- dashboardPage(
  skin = "red",
  dashboardHeader(title = "Net.Security"),
  dashboardSidebar(
    
    sidebarMenu(
      menuItem("Crawler", tabName = "scan", icon = icon("free-code-camp")),
      menuItem("OpenVAS", tabName = "openvas", icon = icon("eye")),
      menuItem("GeoIP", tabName = "geoip", icon = icon("bar-chart")),
      menuItem("CVES", tabName = "searchVuls", icon = icon("bolt")),
      menuItem("Resum", tabName = "resum", icon = icon("thermometer-half"))
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
      tabItem(tabName = "scan",
              fluidRow(
                valueBoxOutput("TotalNikto_Vuls"),
                valueBoxOutput("TotalNmap_Vuls")
              ),
              fluidRow(
                       box(
                         selectInput("selectUrlNikto", label = h3("Nikto"), "")
                       ),
                       box(
                         selectInput("selectUrlNmap", label = h3("Nmap"), "")
                       )
              ),
              h2("Nmap results"),
              dataTableOutput("nmap_vulneravilitis"),
              h2("Nikto results"),
              dataTableOutput("nikto_vulneravilitis")
      ),
      
      # Third tab content
      tabItem(tabName = "geoip",
              leafletOutput("geoip_map",width="100%",height="900px")
              
      ),
      
      # Third tab content
      tabItem(tabName = "openvas",
              fluidRow(
              )
      ),
      
      
      # Fourth tab content
      tabItem(tabName = "searchVuls",
              fluidRow(
                        valueBoxOutput("TotalCVEsinNetSecurity")
              ),
              fluidRow(
                column(width = 12,
                       box(
                         selectInput("selectTipe", label = h3("Search CVEs by type: "), 
                                     choices = list("XSS" = 1, "SQL" = 2, "Authentication" = 3, "CSRF" = 4, "BufferOverFlow" = 5, "None"=6), 
                                     selected = 6)
                       ),
                       box(
                         textInput("CveTextInput", label = h3("Search CVE by Id"), value = "eg: 2016-5195")
                       )
                )
              ),
              fluidRow(
                uiOutput("box_cveID"),
                uiOutput("box_cve_info"),
                uiOutput("box_cve_cvss")
              ),
              dataTableOutput("cvesSearch")
            )
        )
    )
)

server <- function(input, output, session) {
  
  #Configure enviroment
  netSecurity_path <- getwd()
  netWebApp_path <- paste(netSecurity_path, "/net.WebApp", sep = "")
  iconGeoIP_path <- paste(netWebApp_path, "/serverIcon.png", sep = "")
  iconGeoIP_porDos_path <- paste(netWebApp_path, "/serverIcon@2x.png", sep = "")
  path_config_path <- paste(netSecurity_path, "/net.WebApp/R/path_config.R", sep = "")
  source(path_config_path)
  source(confing_enviromet_path)
  
  #Extract info
  t_wVuls <- GetNumberOfVuls()
  
  #Search cves by code
  observeEvent(input$CveTextInput, {
    CVEs_Dataframe <- Search_ConcretCVE(input$CveTextInput)
    #CVE rendertable
    #output$cvesSearch = renderDataTable(
    #  CVEs_Dataframe,
    #  options = list(scrollX = TRUE)
    #)
    #CVE info render
    output$box_cveID <- renderUI({
      box(title = paste("Description of ",  CVEs_Dataframe$cve, sep=" "),
          width = 4, background = "black",
          CVEs_Dataframe$description)
    })
    #CVE info status
    output$box_cve_info <- renderUI({
      box(title = "Info",
          width = 4, background = "black",
          p(CVEs_Dataframe$phase),
          p(CVEs_Dataframe$status),
          p(CVEs_Dataframe$cwe))
    })
    
    #CVE info cvss
    output$box_cve_cvss <- renderUI({
      box(title = "CVSS",
          width = 4, background = "black",
          p(paste("Score ",  CVEs_Dataframe$cvss.score, sep=" ")),
          p(paste("Access vector ",  CVEs_Dataframe$`cvss.access-vector`, sep=" ")),
          p(paste("Authentication ",  CVEs_Dataframe$cvss.authentication, sep=" "))
      )
    })
  })
  #Web vulneraviliti Nikto
  observe({
      updateSelectInput(session, "selectUrlNikto",
      choices = t_wVuls$url
    )})

  #Web vulneraviliti Nikto
  observeEvent(input$selectUrlNikto, {
    webvulsDataframe <- GetVulneravilityNikto_fromUrlDataframe(input$selectUrlNikto)
    output$nikto_vulneravilitis = renderDataTable(
    webvulsDataframe,
    options = list(scrollX = TRUE)
    )
  })

  #Web vulneravility from nmap
  observe({
      updateSelectInput(session, "selectUrlNmap",
      choices = t_wVuls$url
    )})
  
  #Web vulneravility from nmap
  observeEvent(input$selectUrlNmap, {
    nmapvulsDataframe <- GetVulsNMAP_fromUrlDataframe(input$selectUrlNmap)
    output$nmap_vulneravilitis = renderDataTable(
    nmapvulsDataframe,
    options = list(scrollX = TRUE)
    )
  })

  
  #Number of vuls per web
  output$numverofvuls <- renderPlot({
   df2=t_wVuls[order(t_wVuls$Vulneravilitys),]
   df2$url=factor(df2$url,levels=df2$url)
   g <- ggplot(df2,aes(x=factor(url), y=Vulneravilitys, fill=url)) + geom_bar(stat='identity') + labs(y='Vulnerailitys',x='Urls')
   g + ggtitle("Number of vulnerabilities extracted by Nikto from each url") + theme(legend.position="bottom")
  })
  
  #GeoIP Map
  serverIcons <- iconList(
    normal = makeIcon(iconGeoIP_path, iconGeoIP_porDos_path, 50, 50)
  )
  
  output$geoip_map <- renderLeaflet({
    m <- leaflet(geoIP) %>%
      addTiles() %>%  # Add default OpenStreetMap map tiles
      addMarkers(~longitude, ~latitude, popup=paste("<a>",geoIP$ip,"</a>") , icon = ~serverIcons["normal"])
    m
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
  
  #Number of CVEs in Net.Security Dataframes
  output$TotalCVEsinNetSecurity <- renderInfoBox({
    n <- Number_of_CVEs()
    valueBox( n, "CVEs", icon = icon("list"),
      color = "red"
    )
  })
  
  #Number of CVEs in Net.Security Dataframes
  output$TotalNikto_Vuls <- renderInfoBox({
    nk <- Number_of_Nikto_Scans()
    valueBox( nk, "Nikto", icon = icon("list"),
              color = "red"
    )
  })
  
  #Number of CVEs in Net.Security Dataframes
  output$TotalNmap_Vuls <- renderInfoBox({
    np <- Number_of_Nmap_Scans()
    valueBox( np, "Nmap", icon = icon("list"),
              color = "red"
    )
  })
  
}

args = commandArgs(trailingOnly=TRUE)
shinyApp(ui, server, options=list(port = 7777, host = args[1]))
