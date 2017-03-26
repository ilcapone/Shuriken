## app.R ##
library(shiny)
library(shinydashboard)
library(ggplot2)
library(net.security)

ui <- dashboardPage(
  dashboardHeader(title = "Shuriken dashboard"),
  dashboardSidebar(
    
    sidebarMenu(
      menuItem("Dashboard", tabName = "dashboard", icon = icon("dashboard")),
      menuItem("Widgets", tabName = "widgets", icon = icon("th"))
    )
    
  ),
  dashboardBody(
    tabItems(
      # First tab content
      tabItem(tabName = "dashboard",
                
              fluidRow(
                
                box(plotOutput("coolplot", height = 1000),
                    width = 8),
                
                box(
                  title = "Timeline",
                  sliderInput("time_slider", "Time slots:", 1, 100, 50),
                  width = 4)
              )  
      ),
      
      # Second tab content
      tabItem(tabName = "widgets",
              h2("Widgets tab content")
      )
    )
  )
)

server <- function(input, output) { 
  
  #scrapyData <- GetScrapyLinksDataframe()
  
  output$coolplot <- renderPlot({
    
    p1 <- ggplot(scrapyData, aes(x = scrapyData$time, y= scrapyData$urls)) + geom_point()
    p1
    
  })
  
  set.seed(122)
  histdata <- rnorm(500)
  
  output$plot1 <- renderPlot({
    data <- histdata[seq_len(input$slider)]
    hist(data)
  })
  
}

shinyApp(ui, server)
