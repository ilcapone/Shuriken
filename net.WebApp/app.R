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
      
      menuItem("Crawler", tabName = "crawler", icon = icon("thermometer-half")),
      menuItem("WebVul", tabName = "webvul", icon = icon("free-code-camp"))
    )
    
  ),
  dashboardBody(
    tabItems(
      # First tab content
      tabItem(tabName = "crawler",
                
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
      tabItem(tabName = "webvul",
              h2("Widgets tab content")
      )
    )
  )
)

server <- function(input, output) { 
  
  scrapyData <- GetScrapyLinksDataframe()
  
  output$coolplot <- renderPlot({
    
    p1 <- ggplot(scrapyData, aes(x = scrapyData$time, y= scrapyData$url)) + geom_point()
    p1
    
  })
  
}

shinyApp(ui, server)
