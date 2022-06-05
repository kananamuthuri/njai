
library(shiny)
library(shinythemes)


#define Ui
       
 ui <- fluidPage(theme = shinytheme("superhero"),
  
      navbarPage(
              "aema@l",
              
     
     tabpanel(
       sidebarpanel( tags$h3("Input:"),
                     textInput("txt1" , "Given Name:",""),
                     textInput("txt2" , "Surname :","")),
     ))

  ) 
 
 #tab panel & sidepanel

      mainpanel(
        h1("Domain"),
        h3("Output"),
        VerbatimTextOutput("txtout")
      
        )#mainpanel
      
    
      tabpanel("Navbar 2","This panel is intentionally left blank")
      tabpanel("Navbar 3","This panel is intentionally left blank")
      
      # fluidpage end


      server <- function(input, output, session)
        {
        output$txtout <-renderText(
          {paste(input$txt1 ,input$txt2, sep = " ")})
  
}

      
    # create shiny object


shinyApp(ui, server)
