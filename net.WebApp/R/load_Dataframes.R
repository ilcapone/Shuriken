#-------------------------------------------------------------------------------------

######## LOAD OPENVAS DATAFRAME ######

#extract dataframe from openvass.xml
#example scrapyData <- GetScrapyLinksDataframe()
GetOpenVasDataframe <- function (){
  #openvas_path <- "D:/CYBERSECURITY MANAGMENT (Master)/CyS/TFM/ShurikenRepository/data/netSecurity_data/openvas_data.xml"
  opv <- xmlParse(openvas_path)
  nodeCve <- xmlRoot(opv)
  opv_cves <- xpathSApply(nodeCve, "//cve", xmlValue)
  opv_cves <- opv_cves[opv_cves !=  "NOCVE"]
  opv_cves_DF <- data.frame(opv_cves, stringsAsFactors=FALSE)
  cleanColums <- strsplit(opv_cves_DF$opv_cves, split = ", ")
  opvCvesDF <- data.frame(cve=unlist(cleanColums))
  opvCvesDF %>% mutate_if(is.factor, as.character) -> opvCvesDF
  return(opvCvesDF)
}

GetOpenVas_List_DataFrame <- function ()
{
  openvas <- list.files(path = openvas_filesData_path)
  list_openvas <- list()
  print(length(openvas))
  i = 1
  while(i<=length(openvas))
  {
    path <- paste(openvas_filesData_path, openvas[i], sep="/")
    print(path)
    list_openvas[[i]] <- Singlr_OpenVasDataframe(path)
    i = i + 1
  }
  return(list_openvas)
}

Singlr_OpenVasDataframe <- function (openvas_singleFile_path){
  #openvas_path <- "D:/CYBERSECURITY MANAGMENT (Master)/CyS/TFM/ShurikenRepository/data/netSecurity_data/openvas_data.xml"
  opv <- xmlParse(openvas_singleFile_path)
  nodeCve <- xmlRoot(opv)
  opv_cves <- xpathSApply(nodeCve, "//cve", xmlValue)
  opv_cves <- opv_cves[opv_cves !=  "NOCVE"]
  opv_cves_DF <- data.frame(opv_cves, stringsAsFactors=FALSE)
  cleanColums <- strsplit(opv_cves_DF$opv_cves, split = ", ")
  opvCvesDF <- data.frame(cve=unlist(cleanColums))
  opvCvesDF %>% mutate_if(is.factor, as.character) -> opvCvesDF
  return(opvCvesDF)
}

#-------------------------------------------------------------------------------------

######## LOAD CRAWLER DATAFRAME ######

#extract dataframe from crawler_links.cvs
#example scrapyData <- GetScrapyLinksDataframe() 
GetScrapyLinksDataframe <- function() {
  links <- read.csv(crawler_links_path, header=T, sep=",")
  split1=str_split_fixed(links$time, " ", 2)
  time1 <- gsub( ':', '', split1[,2])
  scrapyData <-data.frame("url"=links$url, "urlComes"=links$urlComes,"time"=time1)
  scrapyData %>% mutate_if(is.factor, as.character) -> scrapyData
  return(scrapyData)
}

#extract dataframe from links.cvs
#example vuls <- GetNiktoVulneravilitysDataframe() 
GetNiktoVulneravilitysDataframe <- function(){
  niktoVuls <- read.csv(nikto_crawler_links_path, header=F, sep=",")
  VulsData <- data.frame(matrix(ncol = 6, nrow = 0))
  i=0
  while(i <= nrow(niktoVuls)) {
      VulsData = rbind(VulsData,niktoVuls[i,])
      i= i +1
  }
  x <- c("url", "ip", "port", "osvdb","httpRequest", "urlExtended", "VulInfo" )
  colnames(VulsData) <- x
  VulsData %>% mutate_if(is.factor, as.character) -> VulsData
  VulsData <- filter(VulsData, url != "Nikto - v2.1.6/2.1.5")
  VulsData <- filter(VulsData, ip != "")
  VulsData <- filter(VulsData, url != " and has had a Roman numeral II added to its model number. The previous version")
  return(VulsData)
}

#extract dataframe from links.cvs
#example scan <- GetNmapScanIpDataframe() 
GetNmapScanIpDataframe <- function(){
  nmapScan <- read.csv(nmap_crawler_path, header=F, sep=";")
  VulsData <- data.frame(matrix(ncol = 12, nrow = 0))
  i=0
  while(i <= nrow(nmapScan)) {
      VulsData = rbind(VulsData,nmapScan[i,])
      i= i +1
  }
  x <- c("host","hostname","hostname_type","protocol",
    "port","name","state","product","extrainfo","reason","version","conf","cpe")
  colnames(VulsData) <- x
  VulsData %>% mutate_if(is.factor, as.character) -> VulsData
 
  return(VulsData)
}

GetGeoIPDataframe <- function (){
  geoIPScan <- read.csv(geoIP_crawlerIP_path, header=F, sep=",")
  GeoData <- data.frame(matrix(ncol = 14, nrow = 0))
  i=0
  while(i <= nrow(geoIPScan)) {
    GeoData = rbind(GeoData,geoIPScan[i,])
    i= i +1
  }
  x <- c("city","region_name","ip","region","area_code","time_zone","longitude","metro_code",
         "country_code3","latitude","postal_code","dma_code","country_code","country_name")
  colnames(GeoData) <- x
  GeoData %>% mutate_if(is.factor, as.character) -> GeoData
  GeoData <- filter(GeoData, city != "city")
  GeoData <- transform(GeoData, longitude = as.numeric(longitude), latitude = as.numeric(latitude))
  return(GeoData)
}