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
      menuItem("WebVul", tabName = "webvul", icon = icon("free-code-camp"))
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
              h2("Widgets tab content")
      )
    )
  )
)

server <- function(input, output) { 
  
  t_wVuls <- GetNumberOfVuls()
  
  output$numverofvuls <- renderPlot({
   df2=t_wVuls[order(t_wVuls$Vulneravilitys),]
   df2$url=factor(df2$url,levels=df2$url)
   g <- ggplot(df2,aes(x=factor(url),y=Vulneravilitys)) + geom_bar(stat='identity') + coord_flip() + labs(y='Vulnerailitys',x='url')
   g + ggtitle("Number of vulnerabilities per scanned url") 
  })
  
}

shinyApp(ui, server)
