library(shiny)

ui <- fluidPage( 
  title = "First App",
  tags$h1(
    "Hello World!"
  ),
  
  tags$p(
    rep(c("This is my first paragraph"), times = 10) |> 
      paste(collapse = " ")
  ),
  
  tags$p(
    rep(c("This is my second paragraph"), times = 10) |> 
      paste(collapse = " ")
  )
  
)

server <- function(input, output, session) {
  
}

shinyApp(ui, server)
