
library(stringr)

#extract dataframe from links.cvs
#example scrapyData <- GetScrapyLinksDataframe() 
GetScrapyLinksDataframe <- function() {
  links <- read.csv("data/links.csv", header=T, sep=",")
  linksUrl <- str_split_fixed(links$url, "/", 4)
  split1=str_split_fixed(links$time, " ", 2)
  time1 <- gsub( ':', '', split1[,2])
  scrapyData <-data.frame("urls"=linksUrl[,3],"time"=time1)
  return(scrapyData)
}



