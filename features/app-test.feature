Feature: Todo application testing using selenium
   
   Scenario: Application usage
      Given Users launch chrome browser
      When Users open form webpage
      Then Users add item
      And Users highlight item
      And Users mark item as done
      And Users delete item
      And Users filter active items
      And Users filter done items
      And Users view all tasks