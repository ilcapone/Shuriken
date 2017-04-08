# extract only de info from concret url
GetVulneravility_fromUrlDataframe <- function (parameter){
  parameter <- as.character(parameter)
  VulsData_numer_vuls <- GetNiktoVulneravilitysDataframe()
  VulsData_numer_vuls <- filter(VulsData_numer_vuls, url == parameter)
  return(VulsData_numer_vuls)
}

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
      print(current_url %in% Control_Repeat_Urls)
      print(Control_Repeat_Urls)
      Current_Url_Check <- filter(Numer_VulsData, url == current_url)
      Current_Url_Check <- summarise(Current_Url_Check, url = Current_Url_Check$url[1], Vulneravilitys = sum(Current_Url_Check$Vulneravilitys))
      Tidy_Numer_VulsData = rbind(Tidy_Numer_VulsData,Current_Url_Check)
      new_row = data.frame(current_url)
      Control_Repeat_Urls = rbind(Control_Repeat_Urls,new_row)
      Control_Repeat_Urls %>% mutate_if(is.factor, as.character) -> Control_Repeat_Urls
      print(Tidy_Numer_VulsData)
    }
    i = i +1
  }
  
  colnames(Tidy_Numer_VulsData) <- x
  Tidy_Numer_VulsData <- Tidy_Numer_VulsData[order(Tidy_Numer_VulsData$Vulneravilitys),]
  Tidy_Numer_VulsData %>% mutate_if(is.factor, as.character) -> Tidy_Numer_VulsData
  return(Tidy_Numer_VulsData)
}