#
# This is the user-interface definition of a Shiny web application. You can
# run the application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
# 
#    http://shiny.rstudio.com/
#

library(shiny)
library(ggplot2)
library(dplyr)

# Define UI for application that draws a histogram
shinyUI(fluidPage(
  
  # Application title
  titlePanel("R net.secury WebApp"),
  
  # Sidebar with a slider input for number of bins 
  sidebarLayout(
    sidebarPanel(
       sliderInput("priceInput", "Time", min = 0, max = 100, value = c(25, 40), pre = "$"),
       radioButtons("typeInput", "URLS: ",choices = c("BEER", "REFRESHMENT", "SPIRITS", "WINE"),selected = "WINE"),
       selectInput("countryInput", "Country",choices = c("CANADA", "FRANCE", "ITALY"))
    ),
    
    # Show a plot of the generated distribution
    mainPanel(
      h1('ScrapyCrawler samples'),
      plotOutput("coolplot")
      #br(), br(),
      #tableOutput("results")
    )
  )
))
