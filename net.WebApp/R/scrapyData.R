
library(stringr)

#extract dataframe from crawler_links.cvs
#example scrapyData <- GetScrapyLinksDataframe() 
GetScrapyLinksDataframe <- function() {
  links <- read.csv("data/crawler_links.csv", header=T, sep=",")
  #filtrado de urls
  #linksUrl <- str_split_fixed(links$url, "/", 4)
  split1=str_split_fixed(links$time, " ", 2)
  time1 <- gsub( ':', '', split1[,2])
  #con el filtrado de url
  #scrapyData <-data.frame("url"=linksUrl[,3], "urlComes"=links$urlComes,"time"=time1)
  scrapyData <-data.frame("url"=links$url, "urlComes"=links$urlComes,"time"=time1)
  scrapyData %>% mutate_if(is.factor, as.character) -> scrapyData
  return(scrapyData)
}

#extract dataframe from links.cvs
#example vuls <- GetNiktoVulneravilitysDataframe() 
GetNiktoVulneravilitysDataframe <- function(){
  linksVuls <- read.csv("data/nikto_crawler_links.csv", header=F, sep=",")
  VulsData <- data.frame(matrix(ncol = 6, nrow = 0))
  i=0
  while(i <= nrow(linksVuls)) {
      VulsData = rbind(VulsData,linksVuls[i,])
      i= i +1
  }
  x <- c("url", "ip", "port", "osvdb","httpRequest", "urlExtended", "VulInfo" )
  colnames(VulsData) <- x
  VulsData %>% mutate_if(is.factor, as.character) -> VulsData
  VulsData <- filter(VulsData, url != "Nikto - v2.1.6/2.1.5")
  return(VulsData)
}

GetVulneravility_fromUrlDataframe <- function (parameter){
  parameter <- as.character(parameter)
  VulsData_numer_vuls <- GetNiktoVulneravilitysDataframe()
  VulsData_numer_vuls <- filter(VulsData, url == parameter)
  return(VulsData_numer_vuls)
}

GetNumberOfVuls <- function(){
  
  VulsData_numer_vuls <- GetNiktoVulneravilitysDataframe()
  Numer_VulsData <- data.frame(matrix(ncol = 2, nrow = 0))
  first_url = TRUE
  i=1
  while(i <= nrow(VulsData_numer_vuls)) {
    current_url = VulsData_numer_vuls$url[i]
    if (first_url)
    {
      VulsData = rbind(VulsData,linksVuls[i,])
    }
    i= i +1
  }
  
  x <- c("url", "Vulneravilitys" )
  colnames(Numer_VulsData) <- x
  
}



