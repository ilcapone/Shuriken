
GetVulneravility_fromUrlDataframe <- function (parameter){
  parameter <- as.character(parameter)
  VulsData_numer_vuls <- GetNiktoVulneravilitysDataframe()
  VulsData_numer_vuls <- filter(VulsData_numer_vuls, url == parameter)
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