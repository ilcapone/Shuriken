
library(stringr)
library(ggplot2)
library(net.security)

#install net.security from github devel branch
#devtools::install_github(repo = "r-net-tools/net.security", ref = "devel")

#extract datagrame from net.security pacage
cves <- GetDataFrame("cves")

#extract dataframe from links.cvs
GetScrapyLinksDataframe <- function() {
  links <- read.csv("data/links.csv", header=T, sep=",")
  linksUrl <- str_split_fixed(links$url, "/", 4)
  split1=str_split_fixed(links$time, " ", 2)
  time1 <- gsub( ':', '', split1[,2])
  scrapyData <-data.frame("urls"=linksUrl[,3],"time"=time1)
  return(scrapyData)
}


PlotGrafic <- function()
{
  scrapyData <- GetScrapyLinksDataframe() 
  #geom_line()
  p1 <- ggplot(scrapyData, aes(x = scrapyData$time, y= scrapyData$urls)) + geom_point()
  p1
}



