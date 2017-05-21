#-------------------------------------------------------------------------------------

######## FUNCTIONS FOR CRAWLER EXTRACT INFO #######

# extract only de infoVuls nikcto from concret url
GetVulneravilityNikto_fromUrlDataframe <- function (parameter){
  parameter <- as.character(parameter)
  VulsData_numer_vuls <- GetNiktoVulneravilitysDataframe()
  VulsData_numer_vuls <- filter(VulsData_numer_vuls, url == parameter)
  return(VulsData_numer_vuls)
}

# extract only infoVuls Nmap from url
GetVulsNMAP_fromUrlDataframe <- function(urlParameter){
  #first search IP from url
  search_IP <- GetVulneravilityNikto_fromUrlDataframe(urlParameter)
  ip <- search_IP$ip[1]
  IPParameter <- as.character(ip)
  VulsData_nmap <- GetNmapScanIpDataframe()
  VulsData_nmap <- filter(VulsData_nmap, host == IPParameter)
  return(VulsData_nmap)
}

#Extract the total num of vulneravilitis from nikto for all urls
GetNumberOfVuls <- function(){
  VulsData_numer_vuls <- GetNiktoVulneravilitysDataframe()
  Numer_VulsData <- data.frame(matrix(ncol = 2, nrow = 0))
  CountVuls = 0
  i=1
  current_url = as.character(VulsData_numer_vuls$url[i])
  # Extract info from nikto web vulneravilitys dataframe
  while(i <= nrow(VulsData_numer_vuls)) {
   if (current_url == as.character(VulsData_numer_vuls$url[i])){
     CountVuls = CountVuls +1
   }
   else
   {
     new_row = data.frame(current_url, CountVuls)
     Numer_VulsData = rbind(Numer_VulsData,new_row)
     current_url = as.character(VulsData_numer_vuls$url[i])
     CountVuls = 0
     CountVuls = CountVuls +1
   }
    i= i +1
  }
  x <- c("url", "Vulneravilitys" )
  colnames(Numer_VulsData) <- x
  Numer_VulsData <- Numer_VulsData[order(Numer_VulsData$Vulneravilitys),]
  Numer_VulsData %>% mutate_if(is.factor, as.character) -> Numer_VulsData
  
  # Tidy data from number of vulneravilitys dataframe
  Tidy_Numer_VulsData <- data.frame(matrix(ncol = 2, nrow = 0))
  Control_Repeat_Urls <- data.frame(matrix(ncol = 1, nrow = 0))
  i=1
  while(i <= nrow(Numer_VulsData)) {
    current_url = as.character(Numer_VulsData$url[i])
    if (!(current_url %in% Control_Repeat_Urls$current_url)){
      Current_Url_Check <- filter(Numer_VulsData, url == current_url)
      Current_Url_Check <- summarise(Current_Url_Check, url = Current_Url_Check$url[1], Vulneravilitys = sum(Current_Url_Check$Vulneravilitys))
      Tidy_Numer_VulsData = rbind(Tidy_Numer_VulsData,Current_Url_Check)
      new_row = data.frame(current_url)
      Control_Repeat_Urls = rbind(Control_Repeat_Urls,new_row)
      Control_Repeat_Urls %>% mutate_if(is.factor, as.character) -> Control_Repeat_Urls
    }
    i = i +1
  }
  
  colnames(Tidy_Numer_VulsData) <- x
  Tidy_Numer_VulsData <- Tidy_Numer_VulsData[order(Tidy_Numer_VulsData$Vulneravilitys),]
  Tidy_Numer_VulsData %>% mutate_if(is.factor, as.character) -> Tidy_Numer_VulsData
  Tidy_Numer_VulsData["id"] <-  seq(1, nrow(Tidy_Numer_VulsData), by=1)

  return(Tidy_Numer_VulsData)
}


#-------------------------------------------------------------------------------------

######## FUNCTIONS FOR NET.SECURITY EXTRACT INFO #######
Get_Headers_CVEs <- function(){
  XHeader <- cves[grepl("header", cves$description),]
  return(XHeader)
}

Get_MIME_CVEs <- function(){
  XMIME <- cves[grepl("MIME", cves$description),]
  return(XMIME)
}

Get_MicrosoftVersion_CVEs <- function(version){
  Microsoft <- cves[grepl("Microsoft", cves$description),]
  Microsoft_Version <- Microsoft[grepl(version, Microsoft$cpe.software),]
  return(Microsoft_Version)
}

Get_ApachetVersion_CVEs <- function(version){
  Apache <- cves[grepl("Apache", cves$description),]
  Microsoft_Version <- Microsoft[grepl(version, Apache$cpe.software),]
  return(Microsoft_Version)
}

Get_ASPNET_CVEs <- function(){
  XASPNET <- cves[grepl("ASP.NET", cves$description),]
  return(XASPNET)
}

Get_XSS_CVEs <- function(id){
  if (id==0)
  {
    XSS_CVES <- cves[grepl("XSS", cves$description),]
  }
  else if (id==1)
  {
    XSS_CVES <- cves_Shiny[grepl("XSS", cves_Shiny$description),]
  }
  return(XSS_CVES)
}

Get_SQL_CVEs <- function(id){
  if(id==0)
  {
    sql <- cves[grepl("SQL", cves$description),]
  }
  else if(id==1)
  {
    sql <- cves_Shiny[grepl("SQL", cves_Shiny$description),]
  }
 
  return(sql)
}

Get_Auth_CVEs <- function(id){
  if (id==0)
  {
    auth <- cves[grepl("Authentication", cves$description),]
  }
  else if (id==1)
  {
    auth <- cves_Shiny[grepl("Authentication", cves_Shiny$description),]
  }
  return(auth)
}

Get_CSRF_CVEs <- function(id){
  if (id==0)
  {
    csrf <- cves[grepl("CSRF", cves$description),]
  }
  else if (id==1)
  {
    csrf <- cves_Shiny[grepl("CSRF", cves_Shiny$description),]
  }
  return(csrf)
}

Get_BufferOverFlow_CVEs <- function(id){
  if (id==0)
  {
    buffer <- cves[grepl("Buffer", cves$description),]
  }
  else if (id==1)
  {
    buffer <- cves_Shiny[grepl("Buffer", cves_Shiny$description),]
  }
  return(buffer)
}

CleanCVSS_fromCVEs <- function(){
  cves <- GetDataFrame("cves")
  cvesClean <- separate(cves,cvss, c("cvss.score","cvss.access-vector","cvss.access-complexity","cvss.authentication","cvss.confidentiality-impact","cvss.integrity-impact","cvss.availability-impact","cvss.source","cvss.generated-on-datetime"), sep = ",")
  cvesClean <- separate(cvesClean,cvss.score,c("1","2","3","4","5","cvss.score"), sep='"')
  cvesClean$`1` <- NULL
  cvesClean$`2` <- NULL
  cvesClean$`3` <- NULL
  cvesClean$`4` <- NULL
  cvesClean$`5` <- NULL
  cvesClean <- separate(cvesClean,`cvss.access-vector`,c("1","2","3","cvss.access-vector"), sep='"')
  cvesClean$`1` <- NULL
  cvesClean$`2` <- NULL
  cvesClean$`3` <- NULL
  cvesClean <- separate(cvesClean,`cvss.access-complexity`,c("1","2","3","cvss.access-complexity"), sep='"')
  cvesClean$`1` <- NULL
  cvesClean$`2` <- NULL
  cvesClean$`3` <- NULL
  cvesClean <- separate(cvesClean,`cvss.authentication`,c("1","2","3","cvss.authentication"), sep='"')
  cvesClean$`1` <- NULL
  cvesClean$`2` <- NULL
  cvesClean$`3` <- NULL
  cvesClean <- separate(cvesClean,`cvss.confidentiality-impact`,c("1","2","3","cvss.confidentiality-impact"), sep='"')
  cvesClean$`1` <- NULL
  cvesClean$`2` <- NULL
  cvesClean$`3` <- NULL
  cvesClean <- separate(cvesClean,`cvss.integrity-impact`,c("1","2","3","cvss.integrity-impact"), sep='"')
  cvesClean$`1` <- NULL
  cvesClean$`2` <- NULL
  cvesClean$`3` <- NULL
  cvesClean <- separate(cvesClean,`cvss.availability-impact`,c("1","2","3","cvss.availability-impact"), sep='"')
  cvesClean$`1` <- NULL
  cvesClean$`2` <- NULL
  cvesClean$`3` <- NULL
  cvesClean <- separate(cvesClean,`cvss.source`,c("1","2","3","cvss.source"), sep='"')
  cvesClean$`1` <- NULL
  cvesClean$`2` <- NULL
  cvesClean$`3` <- NULL
  cvesClean <- separate(cvesClean,`cvss.generated-on-datetime`,c("1","2","3","cvss.generated-on-datetime"), sep='"')
  cvesClean$`1` <- NULL
  cvesClean$`2` <- NULL
  cvesClean$`3` <- NULL
  return(cvesClean)
}

CleanCVES_Shiny <- function(){
  cvesShiny <- CleanCVSS_fromCVEs()
  cvesShiny$attack.scenario <- NULL
  cvesShiny$technical.description <- NULL
  cvesShiny$fix.action <- NULL
  cvesShiny$security.protection <- NULL
  cvesShiny$disclosure.datetime <- NULL
  cvesShiny$discovered.datetime <- NULL
  cvesShiny$cpe.software <-NULL
  cvesShiny$cpe.config <- NULL
  cvesShiny$scanner <- NULL
  cvesShiny$comments <- NULL
  cvesShiny$exploit.publish.datetime <- NULL
  return(cvesShiny)
}

#TOFO finish
Select_fromCPE <- function(find_cpe){
  filter_cpe <- filter(cpes, cpe.23 == find_cpe)
  return(filter_cpe)
}