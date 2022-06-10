def wordle():
  while True:
    pWords = ["TODAY", "CODES", "LYING", "WORKS", "WORDS", "SPLIT", "LIKES", "MONEY", "WATCH", "LATCH", "YOUNG", "HOMES", "TRUCE", "TRUCK", "SOLES" , "ENTER", "FOCUS", "POINT", "YOURS", "FOULS", "HOLES", "DYING", "CLOWN", "CLOTH", "TOWEL", "COLTS", "SCOWL", "SEIZE", "SERVE", "SHARP", "SHELF", "SPINE", "SLICE", "SOLID", "SPACE", "STAND", "STONE", "EIGHT", "EARTH", "EAGER", "EBONY", "EDICT", "EIGHT", "ELECT", "ELITE", "ENTRY", "EXTRA", "EVERY", "RIGHT", "HOARD", "CLONE", "SOUTH", "TUBES", "MAILS", "GRAMS", "IMAGE", "VIDEO", "ESSAY", "DRIVE", "READS", "VERGE", "PARKS", "INBOX", "MOVIE", "CLOUD", "BOXES", "SIGHT", "SIGNS", "SIGHS", "SEVEN", "MARVEL", "GAMES", "GAINS", "APPLE", "TALES", "ROLES", "LORES", "ALLOW", "WORLD", "ABOVE", "USING", "CHORE", "PHONE", "ALIGN", "LOADS", "THING", "TOUCH", "VITAL", "PORES", "BOOKS", "WALLS", "ENTER", "COMMA", "SLASH", "LYING", "KILLS", "GUARD", "FREED", "EIGHT", "BRAIN", "MONTH", "SHOTS", "CORES", "SONGS", "SMILE", "BOARS", "GOATS", "BOATS", "CLAIM", "ALIVE", "DEVIL", "GOING", "POINT", "HOIST", "POISE", "POSES", "AGING", "ROOMS", "SMELT", "PLANE", "TEASE", "STUDY", "FILES", "STORE", "THEIR", "STILL", "TIDDY", "TERMS", "TRAIL", "LIGHT", "CARDS" , "PLANT", "FIRES", "WATER", "COLDS", "FORKS", "SPOON", "TIMES", "STOCK", "MARKS", "WRITE", "MICRO", "MACRO", "MINCE", "SQUAD", "ROYAL", "EEEEE", "IRATE", "ADIEU", "MINCE", "MINTS", "FOYER"]
    
    #The word can change. Choice (.choice()) function just chooses a random string element each time**
    import random 
  
    #use for the color text update to remove the use of emoji from the board entirely 
    import colorama
    from colorama import Fore
    from colorama import Style
    from colorama import Back
  
    #when using colorama module, you have to use this command to initialize the colorama module
    colorama.init(autoreset = True)

    import os

    import time
    import timeit

    answer1 = random.choice(pWords)
  
    wordle1 = ["-", "-", "-", "-", "-"]
    wordle2 = ["-", "-", "-", "-", "-"]
    wordle3 = ["-", "-", "-", "-", "-"]
    wordle4 = ["-", "-", "-", "-", "-"]
    wordle5 = ["-", "-", "-", "-", "-"]
    wordle6 = ["-", "-", "-", "-", "-"]

    
    print(Fore.LIGHTGREEN_EX +"W" + Fore.LIGHTYELLOW_EX + "o" + Style.DIM + Fore.WHITE + "r" + Style.NORMAL + Fore.LIGHTGREEN_EX + "d" + Fore.LIGHTYELLOW_EX + "l" + Style.DIM + Fore.WHITE + "e" + Style.NORMAL + Fore.WHITE + ":")
    print(wordle1[0] + " | " + wordle1[1] + " | " + wordle1[2] + " | " + wordle1[3] + " | " + wordle1[4])
    print(wordle2[0] + " "  + "|" + " " + wordle2[1] + " " + "|" + " " + wordle2[2] + " " + "|" + " " + wordle2[3] + " "  + "|" + " " + wordle2[4])
    print(wordle3[0] + " "  + "|" + " " + wordle3[1] + " " + "|" + " " + wordle3[2] + " " + "|" + " " + wordle3[3] + " "  + "|" + " " + wordle3[4])
    print(wordle4[0] + " "  + "|" + " " + wordle4[1] + " " + "|" + " " + wordle4[2] + " " + "|" + " " + wordle4[3] + " "  + "|" + " " + wordle4[4])
    print(wordle5[0] + " "  + "|" + " " + wordle5[1] + " " + "|" + " " + wordle5[2] + " " + "|" + " " + wordle5[3] + " "  + "|" + " " + wordle5[4])
    print(wordle6[0] + " "  + "|" + " " + wordle6[1] + " " + "|" + " " + wordle6[2] + " " + "|" + " " + wordle6[3] + " "  + "|" + " " + wordle6[4])
    
          
    #first guess
    prompt = input("Guess a word: ")
    prompt = list(prompt)
    answer2 = list(answer1)
      
    wordle1[0] = prompt[0]
    wordle1[1] = prompt[1]
    wordle1[2] = prompt[2]
    wordle1[3] = prompt[3]
    wordle1[4] = prompt[4]
  
  
    def corrections1():
      if answer2[0] == wordle1[0]:
        return(Fore.LIGHTGREEN_EX + Style.BRIGHT + wordle1[0])
  
      if answer2[0] != wordle1[0]:
        if wordle1[0] in answer2:
          return(Fore.LIGHTYELLOW_EX + Style.BRIGHT + wordle1[0])
  
        else:
          return(Style.DIM + wordle1[0])
          #Dim/Normal/Brightness changes the color, using Style command
  
    def corrections2():
      if answer2[1] == wordle1[1]:
        return(Fore.LIGHTGREEN_EX + Style.BRIGHT + wordle1[1])
  
      if answer2[1] != wordle1[1]:
        if wordle1[1] in answer2:
          return(Fore.LIGHTYELLOW_EX + Style.BRIGHT + wordle1[1])
  
        else:
          return(Style.DIM + wordle1[1])
  
    def corrections3():
      if answer2[2] == wordle1[2]:
        return(Fore.LIGHTGREEN_EX + Style.BRIGHT + wordle1[2])
  
      if answer2[2] != wordle1[2]:
        if wordle1[2] in answer2:
          return(Fore.LIGHTYELLOW_EX + Style.BRIGHT + wordle1[2])
  
        else:
          return(Style.DIM + wordle1[2])
  
    def corrections4():
      if answer2[3] == wordle1[3]:
        return(Fore.LIGHTGREEN_EX + Style.BRIGHT + wordle1[3])
  
      if answer2[3] != wordle1[3]:
        if wordle1[3] in answer2:
          return(Fore.LIGHTYELLOW_EX + Style.BRIGHT + wordle1[3])
  
        else:
          return(Style.DIM + wordle1[3])
  
    def corrections5():
      if answer2[4] == wordle1[4]:
        return(Fore.LIGHTGREEN_EX + Style.BRIGHT + wordle1[4])
  
      if answer2[4] != wordle1[4]:
        if wordle1[4] in answer2:
          return(Fore.LIGHTYELLOW_EX + Style.BRIGHT + wordle1[4])
  
        else:
          return(Style.DIM + wordle1[4])


    def board1():
      print(Fore.LIGHTGREEN_EX +"W" + Fore.LIGHTYELLOW_EX + "o" + Style.DIM + Fore.WHITE + "r" + Style.NORMAL + Fore.LIGHTGREEN_EX + "d" + Fore.LIGHTYELLOW_EX + "l" + Style.DIM + Fore.WHITE + "e" + Style.NORMAL + Fore.WHITE + ":")
      print(corrections1() + Fore.WHITE + Style.NORMAL +  " | " + corrections2() + Fore.WHITE + Style.NORMAL + " | " + corrections3() + Fore.WHITE + Style.NORMAL + " | " + corrections4() + Fore.WHITE + Style.NORMAL + " | " + corrections5())
      print(wordle2[0] + " "  + "|" + " " + wordle2[1] + " " + "|" + " " + wordle2[2] + " " + "|" + " " + wordle2[3] + " "  + "|" + " " + wordle2[4])
      print(wordle3[0] + " "  + "|" + " " + wordle3[1] + " " + "|" + " " + wordle3[2] + " " + "|" + " " + wordle3[3] + " "  + "|" + " " + wordle3[4])
      print(wordle4[0] + " "  + "|" + " " + wordle4[1] + " " + "|" + " " + wordle4[2] + " " + "|" + " " + wordle4[3] + " "  + "|" + " " + wordle4[4])
      print(wordle5[0] + " "  + "|" + " " + wordle5[1] + " " + "|" + " " + wordle5[2] + " " + "|" + " " + wordle5[3] + " "  + "|" + " " + wordle5[4])
      print(wordle6[0] + " "  + "|" + " " + wordle6[1] + " " + "|" + " " + wordle6[2] + " " + "|" + " " + wordle6[3] + " "  + "|" + " " + wordle6[4])
      
      
    if prompt == answer2:
      os.system('clear')
      board1()
      print(Fore.LIGHTGREEN_EX + "Correct" + Fore.WHITE + ".")
      askResults = input("Would you like to print results?: ")

      if askResults == "Yes" or askResults == "yes":
        def correct():
          if answer2[0] == wordle1[0]:
            return ("🟩")
    
          if answer2[0] != wordle1[0]:
            if wordle1[0] in answer2:
              return ("🟨")
        
            else:
              return ("⬛️")

        def correct1():
          if answer2[1] == wordle1[1]:
            return ("🟩")
        
          if answer2[1] != wordle1[1]:
            if wordle1[1] in answer2:
              return ("🟨")
        
            else:
              return ("⬛️")

        def correct2():
          if answer2[2] == wordle1[2]:
            return ("🟩")
        
          if answer2[2] != wordle1[2]:
            if wordle1[2] in answer2:
              return ("🟨")
        
            else:
              return ("⬛️")

        def correct3():
          if answer2[3] == wordle1[3]:
            return ("🟩")
        
          if answer2[3] != wordle1[3]:
            if wordle1[3] in answer2:
              return ("🟨")
        
            else:
              return ("⬛️")

        def correct4():
          if answer2[4] == wordle1[4]:
            return ("🟩")
        
          if answer2[4] != wordle1[4]:
            if wordle1[4] in answer2:
              return ("🟨")
        
            else:
              return ("⬛️")

        print(" ")
        print("Wordle made by Tharun Dhanabal, 1/6")
        print(correct() + correct1() + correct2() + correct3() + correct4())
        break

      
 
      if askResults == "No" or askResults == "no":
        print(" ")
        print("Alright!")
        break
  
    
    if prompt != answer2:
      os.system('clear')
      board1()
      incorrect = input(Fore.RED + "Incorrect" + Fore.WHITE + ". Guess again: ")
      incorrect = list(incorrect)
        
      wordle2[0] = incorrect[0]
      wordle2[1] = incorrect[1]
      wordle2[2] = incorrect[2]
      wordle2[3] = incorrect[3]
      wordle2[4] = incorrect[4]
  
      def corrections6():
        if answer2[0] == wordle2[0]:
          return(Fore.LIGHTGREEN_EX + Style.BRIGHT + wordle2[0])
    
        if answer2[0] != wordle2[0]:
          if wordle2[0] in answer2:
            return(Fore.LIGHTYELLOW_EX + Style.BRIGHT + wordle2[0])
    
          else:
            return(colorama.Style.DIM + wordle2[0])
  
      def corrections7():
        if answer2[1] == wordle2[1]:
          return(Fore.LIGHTGREEN_EX + Style.BRIGHT + wordle2[1])
    
        if answer2[1] != wordle2[1]:
          if wordle2[1] in answer2:
            return(Fore.LIGHTYELLOW_EX + Style.BRIGHT + wordle2[1])
    
          else:
            return(colorama.Style.DIM + wordle2[1])
    
      def corrections8():
        if answer2[2] == wordle2[2]:
          return(Fore.LIGHTGREEN_EX + Style.BRIGHT + wordle2[2])
    
        if answer2[2] != wordle2[2]:
          if wordle2[2] in answer2:
            return(Fore.LIGHTYELLOW_EX + Style.BRIGHT + wordle2[2])
    
          else:
            return(colorama.Style.DIM + wordle2[2])
    
      def corrections9():
        if answer2[3] == wordle2[3]:
          return(Fore.LIGHTGREEN_EX + Style.BRIGHT + wordle2[3])
    
        if answer2[3] != wordle2[3]:
          if wordle2[3] in answer2:
            return(Fore.LIGHTYELLOW_EX + Style.BRIGHT + wordle2[3])
    
          else:
            return(colorama.Style.DIM + wordle2[3])
    
      def corrections10():
        if answer2[4] == wordle2[4]:
          return(Fore.LIGHTGREEN_EX + Style.BRIGHT + wordle2[4])
    
        if answer2[4] != wordle2[4]:
          if wordle2[4] in answer2:
            return(Fore.LIGHTYELLOW_EX + Style.BRIGHT + wordle2[4])
    
          else:
            return(colorama.Style.DIM + wordle2[4])

      def board2():
        print(Fore.LIGHTGREEN_EX +"W" + Fore.LIGHTYELLOW_EX + "o" + Style.DIM + Fore.WHITE + "r" + Style.NORMAL + Fore.LIGHTGREEN_EX + "d" + Fore.LIGHTYELLOW_EX + "l" + Style.DIM + Fore.WHITE + "e" + Style.NORMAL + Fore.WHITE + ":")
        print(corrections1() + Fore.WHITE + Style.NORMAL +  " | " + corrections2() + Fore.WHITE + Style.NORMAL + " | " + corrections3() + Fore.WHITE + Style.NORMAL + " | " + corrections4() + Fore.WHITE + Style.NORMAL + " | " + corrections5())
        print(corrections6() + Fore.WHITE + Style.NORMAL + " | " + corrections7() + Fore.WHITE + Style.NORMAL + " | " + corrections8() + Fore.WHITE + Style.NORMAL + " | " + corrections9() + Fore.WHITE + Style.NORMAL + " | " + corrections10())
        print(wordle3[0] + " "  + "|" + " " + wordle3[1] + " " + "|" + " " + wordle3[2] + " " + "|" + " " + wordle3[3] + " "  + "|" + " " + wordle3[4])
        print(wordle4[0] + " "  + "|" + " " + wordle4[1] + " " + "|" + " " + wordle4[2] + " " + "|" + " " + wordle4[3] + " "  + "|" + " " + wordle4[4])
        print(wordle5[0] + " "  + "|" + " " + wordle5[1] + " " + "|" + " " + wordle5[2] + " " + "|" + " " + wordle5[3] + " "  + "|" + " " + wordle5[4])
        print(wordle6[0] + " "  + "|" + " " + wordle6[1] + " " + "|" + " " + wordle6[2] + " " + "|" + " " + wordle6[3] + " "  + "|" + " " + wordle6[4])
        
      if incorrect == answer2:
        os.system('clear')
        board2()
        print(Fore.LIGHTGREEN_EX + "Correct" + Fore.WHITE + ".")
        askResults = input("Would you like to print results?: ")

        if askResults == "Yes" or askResults == "yes":
          def correct():
            if answer2[0] == wordle1[0]:
              return ("🟩")
      
            if answer2[0] != wordle1[0]:
              if wordle1[0] in answer2:
                return ("🟨")
          
              else:
                return ("⬛️")
  
          def correct1():
            if answer2[1] == wordle1[1]:
              return ("🟩")
          
            if answer2[1] != wordle1[1]:
              if wordle1[1] in answer2:
                return ("🟨")
          
              else:
                return ("⬛️")
  
          def correct2():
            if answer2[2] == wordle1[2]:
              return ("🟩")
          
            if answer2[2] != wordle1[2]:
              if wordle1[2] in answer2:
                return ("🟨")
          
              else:
                return ("⬛️")
  
          def correct3():
            if answer2[3] == wordle1[3]:
              return ("🟩")
          
            if answer2[3] != wordle1[3]:
              if wordle1[3] in answer2:
                return ("🟨")
          
              else:
                return ("⬛️")
  
          def correct4():
            if answer2[4] == wordle1[4]:
              return ("🟩")
          
            if answer2[4] != wordle1[4]:
              if wordle1[4] in answer2:
                return ("🟨")
          
              else:
                return ("⬛️")

          def correct5():
            if answer2[0] == wordle2[0]:
              return ("🟩")
              
          
            if answer2[0] != wordle2[0]:
              if wordle2[0] in answer2:
                return ("🟨")
          
              else:
                return ("⬛️")
          
          def correct6():
            if answer2[1] == wordle2[1]:
              return ("🟩")
          
            if answer2[1] != wordle2[1]:
              if wordle2[1] in answer2:
                return ("🟨")
          
              else:
                return("⬛️")
          
          def correct7():
            if answer2[2] == wordle2[2]:
              return ("🟩")
          
            if answer2[2] != wordle2[2]:
              if wordle2[2] in answer2:
                return ("🟨")
          
              else:
                return ("⬛️")
          
          def correct8():
            if answer2[3] == wordle2[3]:
              return ("🟩")
          
            if answer2[3] != wordle2[3]:
              if wordle2[3] in answer2:
                return ("🟨")
          
              else:
                return ("⬛️")
          
          def correct9():
            if answer2[4] == wordle2[4]:
              return ("🟩")
          
            if answer2[4] != wordle2[4]:
              if wordle2[4] in answer2:
                return ("🟨")
          
              else: 
                return ("⬛️")

          print(" ")
          print("Wordle made by Tharun Dhanabal, 2/6")
          print(correct() + correct1() + correct2() + correct3() + correct4())
          print(correct5() + correct6() + correct7() + correct8() + correct9())
          break


        if askResults == "No" or askResults == "no":
          print(" ")
          print("Alright!")
          break
  
      
      if incorrect != answer2:
        os.system('clear')
        board2()
        incorrect2 = input(Fore.RED + "Incorrect" + Fore.WHITE + ". Guess again: ")
        incorrect2 = list(incorrect2)
          
        wordle3[0] = incorrect2[0]
        wordle3[1] = incorrect2[1]
        wordle3[2] = incorrect2[2]
        wordle3[3] = incorrect2[3]
        wordle3[4] = incorrect2[4]
  
        def corrections11():
          if answer2[0] == wordle3[0]:
            return(Fore.LIGHTGREEN_EX + Style.BRIGHT + wordle3[0])
      
          if answer2[0] != wordle3[0]:
            if wordle3[0] in answer2:
              return(Fore.LIGHTYELLOW_EX + Style.BRIGHT + wordle3[0])
      
            else:
              return(colorama.Style.DIM + wordle3[0])
  
        def corrections12():
          if answer2[1] == wordle3[1]:
            return(Fore.LIGHTGREEN_EX + Style.BRIGHT + wordle3[1])
      
          if answer2[1] != wordle3[1]:
            if wordle3[1] in answer2:
              return(Fore.LIGHTYELLOW_EX + Style.BRIGHT + wordle3[1])
      
            else:
              return(colorama.Style.DIM + wordle3[1])
    
        def corrections13():
          if answer2[2] == wordle3[2]:
            return(Fore.LIGHTGREEN_EX + Style.BRIGHT + wordle3[2])
      
          if answer2[2] != wordle3[2]:
            if wordle3[2] in answer2:
              return(Fore.LIGHTYELLOW_EX + Style.BRIGHT + wordle3[2])
      
            else:
              return(colorama.Style.DIM + wordle3[2])
    
        def corrections14():
          if answer2[3] == wordle3[3]:
            return(Fore.LIGHTGREEN_EX + Style.BRIGHT + wordle3[3])
      
          if answer2[3] != wordle3[3]:
            if wordle3[3] in answer2:
              return(Fore.LIGHTYELLOW_EX + Style.BRIGHT + wordle3[3])
      
            else:
              return(colorama.Style.DIM + wordle3[3])
    
        def corrections15():
          if answer2[4] == wordle3[4]:
            return(Fore.LIGHTGREEN_EX + Style.BRIGHT + wordle3[4])
      
          if answer2[4] != wordle3[4]:
            if wordle3[4] in answer2:
              return(Fore.LIGHTYELLOW_EX + Style.BRIGHT + wordle3[4])
      
            else:
              return(colorama.Style.DIM + wordle3[4])

        
        def board3():
          print(Fore.LIGHTGREEN_EX +"W" + Fore.LIGHTYELLOW_EX + "o" + Style.DIM + Fore.WHITE + "r" + Style.NORMAL + Fore.LIGHTGREEN_EX + "d" + Fore.LIGHTYELLOW_EX + "l" + Style.DIM + Fore.WHITE + "e" + Style.NORMAL + Fore.WHITE + ":")
          print(corrections1() + Fore.WHITE + Style.NORMAL +  " | " + corrections2() + Fore.WHITE + Style.NORMAL + " | " + corrections3() + Fore.WHITE + Style.NORMAL + " | " + corrections4() + Fore.WHITE + Style.NORMAL + " | " + corrections5())
          print(corrections6() + Fore.WHITE + Style.NORMAL + " | " + corrections7() + Fore.WHITE + Style.NORMAL + " | " + corrections8() + Fore.WHITE + Style.NORMAL + " | " + corrections9() + Fore.WHITE + Style.NORMAL + " | " + corrections10())
          print(corrections11() + Fore.WHITE + Style.NORMAL + " | " + corrections12() + Fore.WHITE + Style.NORMAL + " | " + corrections13() + Fore.WHITE + Style.NORMAL + " | " + corrections14() + Fore.WHITE + Style.NORMAL + " | " + corrections15()) 
          print(wordle4[0] + " "  + "|" + " " + wordle4[1] + " " + "|" + " " + wordle4[2] + " " + "|" + " " + wordle4[3] + " "  + "|" + " " + wordle4[4])
          print(wordle5[0] + " "  + "|" + " " + wordle5[1] + " " + "|" + " " + wordle5[2] + " " + "|" + " " + wordle5[3] + " "  + "|" + " " + wordle5[4])
          print(wordle6[0] + " "  + "|" + " " + wordle6[1] + " " + "|" + " " + wordle6[2] + " " + "|" + " " + wordle6[3] + " "  + "|" + " " + wordle6[4])
  
        if incorrect2 == answer2:
          os.system()
          board3()
          print(Fore.LIGHTGREEN_EX + "Correct" + Fore.WHITE + ".")
          askResults = input("Would you like to print results?: ")
  
          if askResults == "Yes" or askResults == "yes":
            def correct():
              if answer2[0] == wordle1[0]:
                return ("🟩")
        
              if answer2[0] != wordle1[0]:
                if wordle1[0] in answer2:
                  return ("🟨")
            
                else:
                  return ("⬛️")
    
            def correct1():
              if answer2[1] == wordle1[1]:
                return ("🟩")
            
              if answer2[1] != wordle1[1]:
                if wordle1[1] in answer2:
                  return ("🟨")
            
                else:
                  return ("⬛️")
    
            def correct2():
              if answer2[2] == wordle1[2]:
                return ("🟩")
            
              if answer2[2] != wordle1[2]:
                if wordle1[2] in answer2:
                  return ("🟨")
            
                else:
                  return ("⬛️")
    
            def correct3():
              if answer2[3] == wordle1[3]:
                return ("🟩")
            
              if answer2[3] != wordle1[3]:
                if wordle1[3] in answer2:
                  return ("🟨")
            
                else:
                  return ("⬛️")
    
            def correct4():
              if answer2[4] == wordle1[4]:
                return ("🟩")
            
              if answer2[4] != wordle1[4]:
                if wordle1[4] in answer2:
                  return ("🟨")
            
                else:
                  return ("⬛️")
  
            def correct5():
              if answer2[0] == wordle2[0]:
                return ("🟩")
                
            
              if answer2[0] != wordle2[0]:
                if wordle2[0] in answer2:
                  return ("🟨")
            
                else:
                  return ("⬛️")
            
            def correct6():
              if answer2[1] == wordle2[1]:
                return ("🟩")
            
              if answer2[1] != wordle2[1]:
                if wordle2[1] in answer2:
                  return ("🟨")
            
                else:
                  return("⬛️")
            
            def correct7():
              if answer2[2] == wordle2[2]:
                return ("🟩")
            
              if answer2[2] != wordle2[2]:
                if wordle2[2] in answer2:
                  return ("🟨")
            
                else:
                  return ("⬛️")
            
            def correct8():
              if answer2[3] == wordle2[3]:
                return ("🟩")
            
              if answer2[3] != wordle2[3]:
                if wordle2[3] in answer2:
                  return ("🟨")
            
                else:
                  return ("⬛️")
            
            def correct9():
              if answer2[4] == wordle2[4]:
                return ("🟩")
            
              if answer2[4] != wordle2[4]:
                if wordle2[4] in answer2:
                  return ("🟨")
            
                else: 
                  return ("⬛️")

            def correct10():
              if answer2[0] == wordle3[0]:
                return ("🟩")
                
            
              if answer2[0] != wordle3[0]:
                if wordle3[0] in answer2: 
                  return ("🟨")
            
                else:
                  return ("⬛️")
            
            def correct11():
              if answer2[1] == wordle3[1]:
                return ("🟩")
            
              if answer2[1] != wordle3[1]:
                if wordle3[1] in answer2:
                  return ("🟨")
            
                else:
                  return ("⬛️")
      
            def correct12():
              if answer2[2] == wordle3[2]:
                return ("🟩")
      
              if answer2[2] != wordle3[2]:
                if wordle3[2] in answer2:
                  return ("🟨")
      
                else:
                  return ("⬛️")
      
            def correct13():
              if answer2[3] == wordle3[3]:
                return ("🟩")
      
              if answer2[3] != wordle3[3]:
                if wordle3[3] in answer2:
                  return ("🟨")
      
                else:
                  return ("⬛️")
      
            def correct14():
              if answer2[4] == wordle3[4]:
                return ("🟩")
      
              if answer2[4] != wordle3[4]:
                if wordle2[4] in answer2:
                  return ("🟨")
      
                else: 
                  return ("⬛️")

  
            print(" ")
            print("Wordle made by Tharun Dhanabal, 3/6")
            print(correct() + correct1() + correct2() + correct3() + correct4())
            print(correct5() + correct6() + correct7() + correct8() + correct9())
            print(correct10() + correct11() + correct12() + correct13 + correct14())
            break
  
  
          if askResults == "No" or askResults == "no":
            print(" ")
            print("Alright!")
            break
    
          
        if incorrect2 != answer2:
          os.system('clear')
          board3()
          incorrect3 = input(Fore.RED + "Incorrect" + Fore.WHITE + ". Guess again: ")
          incorrect3 = list(incorrect3)
    
          wordle4[0] = incorrect3[0]
          wordle4[1] = incorrect3[1]
          wordle4[2] = incorrect3[2]
          wordle4[3] = incorrect3[3]
          wordle4[4] = incorrect3[4]
  
          def corrections16():
            if answer2[0] == wordle4[0]:
              return(Fore.LIGHTGREEN_EX + Style.BRIGHT + wordle4[0])
        
            if answer2[0] != wordle4[0]:
              if wordle4[0] in answer2:
                return(Fore.LIGHTYELLOW_EX + Style.BRIGHT + wordle4[0])
        
              else:
                return(colorama.Style.DIM + wordle4[0])
  
          def corrections17():
            if answer2[1] == wordle4[1]:
              return(Fore.LIGHTGREEN_EX + Style.BRIGHT + wordle4[1])
        
            if answer2[1] != wordle4[1]:
              if wordle4[1] in answer2:
                return(Fore.LIGHTYELLOW_EX + Style.BRIGHT + wordle4[1])
        
              else:
                return(colorama.Style.DIM + wordle4[1])
      
          def corrections18():
            if answer2[2] == wordle4[2]:
              return(Fore.LIGHTGREEN_EX + Style.BRIGHT + wordle4[2])
        
            if answer2[2] != wordle4[2]:
              if wordle4[2] in answer2:
                return(Fore.LIGHTYELLOW_EX + Style.BRIGHT + wordle4[2])
        
              else:
                return(colorama.Style.DIM + wordle4[2])
      
          def corrections19():
            if answer2[3] == wordle4[3]:
              return(Fore.LIGHTGREEN_EX + Style.BRIGHT + wordle4[3])
        
            if answer2[3] != wordle4[3]:
              if wordle4[3] in answer2:
                return(Fore.LIGHTYELLOW_EX + Style.BRIGHT + wordle4[3])
        
              else:
                return(colorama.Style.DIM + wordle4[3])
      
          def corrections20():
            if answer2[4] == wordle4[4]:
              return(Fore.LIGHTGREEN_EX + Style.BRIGHT + wordle4[4])
        
            if answer2[4] != wordle4[4]:
              if wordle4[4] in answer2:
                return(Fore.LIGHTYELLOW_EX + Style.BRIGHT + wordle4[4])
        
              else:
                return(colorama.Style.DIM + wordle4[4])  

    
          def board4():
            print(Fore.LIGHTGREEN_EX +"W" + Fore.LIGHTYELLOW_EX + "o" + Style.DIM + Fore.WHITE + "r" + Style.NORMAL + Fore.LIGHTGREEN_EX + "d" + Fore.LIGHTYELLOW_EX + "l" + Style.DIM + Fore.WHITE + "e" + Style.NORMAL + Fore.WHITE + ":")
            print(corrections1() + Fore.WHITE + Style.NORMAL +  " | " + corrections2() + Fore.WHITE + Style.NORMAL + " | " + corrections3() + Fore.WHITE + Style.NORMAL + " | " + corrections4() + Fore.WHITE + Style.NORMAL + " | " + corrections5() + Fore.WHITE + Style.NORMAL)
            print(corrections6() + Fore.WHITE + Style.NORMAL + " | " + corrections7() + Fore.WHITE + Style.NORMAL + " | " + corrections8() + Fore.WHITE + Style.NORMAL + " | " + corrections9() + Fore.WHITE + Style.NORMAL + " | " + corrections10() + Fore.WHITE + Style.NORMAL)
            print(corrections11() + Fore.WHITE + Style.NORMAL + " | " + corrections12() + Fore.WHITE + Style.NORMAL + " | " + corrections13() + Fore.WHITE + Style.NORMAL + " | " + corrections14() + Fore.WHITE + Style.NORMAL + " | " + corrections15())
            print(corrections16() + Fore.WHITE + Style.NORMAL + " | " + corrections17() + Fore.WHITE + Style.NORMAL + " | " + corrections18() + Fore.WHITE + Style.NORMAL + " | " + corrections19() + Fore.WHITE + Style.NORMAL + " | " + corrections20())
            print(wordle5[0] + " "  + "|" + " " + wordle5[1] + " " + "|" + " " + wordle5[2] + " " + "|" + " " + wordle5[3] + " "  + "|" + " " + wordle5[4])
            print(wordle6[0] + " "  + "|" + " " + wordle6[1] + " " + "|" + " " + wordle6[2] + " " + "|" + " " + wordle6[3] + " "  + "|" + " " + wordle6[4])
            
      
          if incorrect3 == answer2:
            os.system('clear')
            board4()
            print(Fore.LIGHTGREEN_EX + "Correct" + Fore.WHITE + ".")

            askResults = input("Would you like to print results?: ")
    
            if askResults == "Yes" or askResults == "yes":
              def correct():
                if answer2[0] == wordle1[0]:
                  return ("🟩")
          
                if answer2[0] != wordle1[0]:
                  if wordle1[0] in answer2:
                    return ("🟨")
              
                  else:
                    return ("⬛️")
      
              def correct1():
                if answer2[1] == wordle1[1]:
                  return ("🟩")
              
                if answer2[1] != wordle1[1]:
                  if wordle1[1] in answer2:
                    return ("🟨")
              
                  else:
                    return ("⬛️")
      
              def correct2():
                if answer2[2] == wordle1[2]:
                  return ("🟩")
              
                if answer2[2] != wordle1[2]:
                  if wordle1[2] in answer2:
                    return ("🟨")
              
                  else:
                    return ("⬛️")
      
              def correct3():
                if answer2[3] == wordle1[3]:
                  return ("🟩")
              
                if answer2[3] != wordle1[3]:
                  if wordle1[3] in answer2:
                    return ("🟨")
              
                  else:
                    return ("⬛️")
      
              def correct4():
                if answer2[4] == wordle1[4]:
                  return ("🟩")
              
                if answer2[4] != wordle1[4]:
                  if wordle1[4] in answer2:
                    return ("🟨")
              
                  else:
                    return ("⬛️")
    
              def correct5():
                if answer2[0] == wordle2[0]:
                  return ("🟩")
                  
              
                if answer2[0] != wordle2[0]:
                  if wordle2[0] in answer2:
                    return ("🟨")
              
                  else:
                    return ("⬛️")
              
              def correct6():
                if answer2[1] == wordle2[1]:
                  return ("🟩")
              
                if answer2[1] != wordle2[1]:
                  if wordle2[1] in answer2:
                    return ("🟨")
              
                  else:
                    return("⬛️")
              
              def correct7():
                if answer2[2] == wordle2[2]:
                  return ("🟩")
              
                if answer2[2] != wordle2[2]:
                  if wordle2[2] in answer2:
                    return ("🟨")
              
                  else:
                    return ("⬛️")
              
              def correct8():
                if answer2[3] == wordle2[3]:
                  return ("🟩")
              
                if answer2[3] != wordle2[3]:
                  if wordle2[3] in answer2:
                    return ("🟨")
              
                  else:
                    return ("⬛️")
              
              def correct9():
                if answer2[4] == wordle2[4]:
                  return ("🟩")
              
                if answer2[4] != wordle2[4]:
                  if wordle2[4] in answer2:
                    return ("🟨")
              
                  else: 
                    return ("⬛️")
  
              def correct10():
                if answer2[0] == wordle3[0]:
                  return ("🟩")
                  
              
                if answer2[0] != wordle3[0]:
                  if wordle3[0] in answer2: 
                    return ("🟨")
              
                  else:
                    return ("⬛️")
              
              def correct11():
                if answer2[1] == wordle3[1]:
                  return ("🟩")
              
                if answer2[1] != wordle3[1]:
                  if wordle3[1] in answer2:
                    return ("🟨")
              
                  else:
                    return ("⬛️")
        
              def correct12():
                if answer2[2] == wordle3[2]:
                  return ("🟩")
        
                if answer2[2] != wordle3[2]:
                  if wordle3[2] in answer2:
                    return ("🟨")
        
                  else:
                    return ("⬛️")
        
              def correct13():
                if answer2[3] == wordle3[3]:
                  return ("🟩")
        
                if answer2[3] != wordle3[3]:
                  if wordle3[3] in answer2:
                    return ("🟨")
        
                  else:
                    return ("⬛️")
        
              def correct14():
                if answer2[4] == wordle3[4]:
                  return ("🟩")
        
                if answer2[4] != wordle3[4]:
                  if wordle2[4] in answer2:
                    return ("🟨")
        
                  else: 
                    return ("⬛️")

              def correct15():
                if answer2[0] == wordle4[0]:
                  return ("🟩")
                    
                
                if answer2[0] != wordle4[0]:
                  if wordle4[0] in answer2:
                    return ("🟨")
                
                  else:
                    return ("⬛️")
              
              def correct16():
                if answer2[1] == wordle4[1]:
                  return ("🟩")
              
                if answer2[1] != wordle4[1]:
                  if wordle4[1] in answer2:
                    return ("🟨")
              
                  else:
                    return("⬛️")
              
              def correct17():
                if answer2[2] == wordle4[2]:
                  return ("🟩")
              
                if answer2[2] != wordle4[2]:
                  if wordle4[2] in answer2:
                    return ("🟨")
              
                  else:
                    return ("⬛️")
              
              def correct18():
                if answer2[3] == wordle4[3]:
                  return("🟩")
              
                if answer2[3] != wordle4[3]:
                  if wordle4[3] in answer2:
                    return ("🟨")
              
                  else:
                    return ("⬛️")
              
              def correct19():
                if answer2[4] == wordle4[4]:
                  return ("🟩")
              
                if answer2[4] != wordle4[4]:
                  if wordle4[4] in answer2:
                    return ("🟨")
                          
                  else:
                    return ("⬛️")

  
              print(" ")
              print("Wordle made by Tharun Dhanabal, 4/6")
              print(correct() + correct1() + correct2() + correct3() + correct4())
              print(correct5() + correct6() + correct7() + correct8() + correct9())
              print(correct10() + correct11() + correct12() + correct13() + correct14())
              print(correct15() + correct16() + correct17() + correct18() + correct19())
              break

  
            if askResults == "No" or askResults == "no":
              print(" ")
              print("Alright!")
              break
  
          
          if incorrect3 != answer2:
            os.system('clear')
            board4()
            incorrect4 = input(Fore.RED + "Incorrect" + Fore.WHITE + ". Guess again: ")
            incorrect4 = list(incorrect4)
              
            wordle5[0] = incorrect4[0]
            wordle5[1] = incorrect4[1]
            wordle5[2] = incorrect4[2]
            wordle5[3] = incorrect4[3]
            wordle5[4] = incorrect4[4]
  
            def corrections21():
              if answer2[0] == wordle5[0]:
                return(Fore.LIGHTGREEN_EX + Style.BRIGHT + wordle5[0])
          
              if answer2[0] != wordle5[0]:
                if wordle5[0] in answer2:
                  return(Fore.LIGHTYELLOW_EX + Style.BRIGHT + wordle5[0])
          
                else:
                  return(colorama.Style.DIM + wordle5[0])
  
            def corrections22():
              if answer2[1] == wordle5[1]:
                return(Fore.LIGHTGREEN_EX + Style.BRIGHT + wordle5[1])
          
              if answer2[1] != wordle5[1]:
                if wordle5[1] in answer2:
                  return(Fore.LIGHTYELLOW_EX + Style.BRIGHT + wordle5[1])
          
                else:
                  return(colorama.Style.DIM + wordle5[1])
        
            def corrections23():
              if answer2[2] == wordle5[2]:
                return(Fore.LIGHTGREEN_EX + Style.BRIGHT + wordle5[2])
          
              if answer2[2] != wordle5[2]:
                if wordle5[2] in answer2:
                  return(Fore.LIGHTYELLOW_EX + Style.BRIGHT + wordle5[2])
          
                else:
                  return(colorama.Style.DIM + wordle5[2])
        
            def corrections24():
              if answer2[3] == wordle5[3]:
                return(Fore.LIGHTGREEN_EX + Style.BRIGHT + wordle5[3])
          
              if answer2[3] != wordle5[3]:
                if wordle4[3] in answer2:
                  return(Fore.LIGHTYELLOW_EX + Style.BRIGHT + wordle5[3])
          
                else:
                  return(colorama.Style.DIM + wordle5[3])
        
            def corrections25():
              if answer2[4] == wordle5[4]:
                return(Fore.LIGHTGREEN_EX + Style.BRIGHT + wordle5[4])
          
              if answer2[4] != wordle5[4]:
                if wordle5[4] in answer2:
                  return(Fore.LIGHTYELLOW_EX + Style.BRIGHT + wordle5[4])
          
                else:
                  return(colorama.Style.DIM + wordle5[4])

            
            def board5():
              print(Fore.LIGHTGREEN_EX +"W" + Fore.LIGHTYELLOW_EX + "o" + Style.DIM + Fore.WHITE + "r" + Style.NORMAL + Fore.LIGHTGREEN_EX + "d" + Fore.LIGHTYELLOW_EX + "l" + Style.DIM + Fore.WHITE + "e" + Style.NORMAL + Fore.WHITE + ":")
              print(corrections1() + Fore.WHITE + Style.NORMAL +  " | " + corrections2() + Fore.WHITE + Style.NORMAL + " | " + corrections3() + Fore.WHITE + Style.NORMAL + " | " + corrections4() + Fore.WHITE + Style.NORMAL + " | " + corrections5() + Fore.WHITE + Style.NORMAL)
              print(corrections6() + Fore.WHITE + Style.NORMAL + " | " + corrections7() + Fore.WHITE + Style.NORMAL + " | " + corrections8() + Fore.WHITE + Style.NORMAL + " | " + corrections9() + Fore.WHITE + Style.NORMAL + " | " + corrections10() + Fore.WHITE + Style.NORMAL)
              print(corrections11() + Fore.WHITE + Style.NORMAL + " | " + corrections12() + Fore.WHITE + Style.NORMAL + " | " + corrections13() + Fore.WHITE + Style.NORMAL + " | " + corrections14() + Fore.WHITE + Style.NORMAL + " | " + corrections15())
              print(corrections16() + Fore.WHITE + Style.NORMAL + " | " + corrections17() + Fore.WHITE + Style.NORMAL + " | " + corrections18() + Fore.WHITE + Style.NORMAL + " | " + corrections19() + Fore.WHITE + Style.NORMAL + " | " + corrections20())
              print(corrections21() + Fore.WHITE + Style.NORMAL + " | " + corrections22() + Fore.WHITE + Style.NORMAL + " | " + corrections23() + Fore.WHITE + Style.NORMAL + " | " + corrections24() + Fore.WHITE + Style.NORMAL + " | " + corrections25())
              print(wordle6[0] + " "  + "|" + " " + wordle6[1] + " " + "|" + " " + wordle6[2] + " " + "|" + " " + wordle6[3] + " "  + "|" + " " + wordle6[4])

            
            if incorrect4 == answer2:
              os.system('clear')
              board5()
              print(Fore.LIGHTGREEN_EX + "Correct" + Fore.WHITE + ".")
  
              askResults = input("Would you like to print results?: ")
      
              if askResults == "Yes" or askResults == "yes":
                def correct():
                  if answer2[0] == wordle1[0]:
                    return ("🟩")
            
                  if answer2[0] != wordle1[0]:
                    if wordle1[0] in answer2:
                      return ("🟨")
                
                    else:
                      return ("⬛️")
        
                def correct1():
                  if answer2[1] == wordle1[1]:
                    return ("🟩")
                
                  if answer2[1] != wordle1[1]:
                    if wordle1[1] in answer2:
                      return ("🟨")
                
                    else:
                      return ("⬛️")
        
                def correct2():
                  if answer2[2] == wordle1[2]:
                    return ("🟩")
                
                  if answer2[2] != wordle1[2]:
                    if wordle1[2] in answer2:
                      return ("🟨")
                
                    else:
                      return ("⬛️")
        
                def correct3():
                  if answer2[3] == wordle1[3]:
                    return ("🟩")
                
                  if answer2[3] != wordle1[3]:
                    if wordle1[3] in answer2:
                      return ("🟨")
                
                    else:
                      return ("⬛️")
        
                def correct4():
                  if answer2[4] == wordle1[4]:
                    return ("🟩")
                
                  if answer2[4] != wordle1[4]:
                    if wordle1[4] in answer2:
                      return ("🟨")
                
                    else:
                      return ("⬛️")
      
                def correct5():
                  if answer2[0] == wordle2[0]:
                    return ("🟩")
                    
                
                  if answer2[0] != wordle2[0]:
                    if wordle2[0] in answer2:
                      return ("🟨")
                
                    else:
                      return ("⬛️")
                
                def correct6():
                  if answer2[1] == wordle2[1]:
                    return ("🟩")
                
                  if answer2[1] != wordle2[1]:
                    if wordle2[1] in answer2:
                      return ("🟨")
                
                    else:
                      return("⬛️")
                
                def correct7():
                  if answer2[2] == wordle2[2]:
                    return ("🟩")
                
                  if answer2[2] != wordle2[2]:
                    if wordle2[2] in answer2:
                      return ("🟨")
                
                    else:
                      return ("⬛️")
                
                def correct8():
                  if answer2[3] == wordle2[3]:
                    return ("🟩")
                
                  if answer2[3] != wordle2[3]:
                    if wordle2[3] in answer2:
                      return ("🟨")
                
                    else:
                      return ("⬛️")
                
                def correct9():
                  if answer2[4] == wordle2[4]:
                    return ("🟩")
                
                  if answer2[4] != wordle2[4]:
                    if wordle2[4] in answer2:
                      return ("🟨")
                
                    else: 
                      return ("⬛️")
    
                def correct10():
                  if answer2[0] == wordle3[0]:
                    return ("🟩")
                    
                
                  if answer2[0] != wordle3[0]:
                    if wordle3[0] in answer2: 
                      return ("🟨")
                
                    else:
                      return ("⬛️")
                
                def correct11():
                  if answer2[1] == wordle3[1]:
                    return ("🟩")
                
                  if answer2[1] != wordle3[1]:
                    if wordle3[1] in answer2:
                      return ("🟨")
                
                    else:
                      return ("⬛️")
          
                def correct12():
                  if answer2[2] == wordle3[2]:
                    return ("🟩")
          
                  if answer2[2] != wordle3[2]:
                    if wordle3[2] in answer2:
                      return ("🟨")
          
                    else:
                      return ("⬛️")
          
                def correct13():
                  if answer2[3] == wordle3[3]:
                    return ("🟩")
          
                  if answer2[3] != wordle3[3]:
                    if wordle3[3] in answer2:
                      return ("🟨")
          
                    else:
                      return ("⬛️")
          
                def correct14():
                  if answer2[4] == wordle3[4]:
                    return ("🟩")
          
                  if answer2[4] != wordle3[4]:
                    if wordle2[4] in answer2:
                      return ("🟨")
          
                    else: 
                      return ("⬛️")
  
                def correct15():
                  if answer2[0] == wordle4[0]:
                    return ("🟩")
                      
                  
                  if answer2[0] != wordle4[0]:
                    if wordle4[0] in answer2:
                      return ("🟨")
                  
                    else:
                      return ("⬛️")
                
                def correct16():
                  if answer2[1] == wordle4[1]:
                    return ("🟩")
                
                  if answer2[1] != wordle4[1]:
                    if wordle4[1] in answer2:
                      return ("🟨")
                
                    else:
                      return("⬛️")
                
                def correct17():
                  if answer2[2] == wordle4[2]:
                    return ("🟩")
                
                  if answer2[2] != wordle4[2]:
                    if wordle4[2] in answer2:
                      return ("🟨")
                
                    else:
                      return ("⬛️")
                
                def correct18():
                  if answer2[3] == wordle4[3]:
                    return("🟩")
                
                  if answer2[3] != wordle4[3]:
                    if wordle4[3] in answer2:
                      return ("🟨")
                
                    else:
                      return ("⬛️")
                
                def correct19():
                  if answer2[4] == wordle4[4]:
                    return ("🟩")
                
                  if answer2[4] != wordle4[4]:
                    if wordle4[4] in answer2:
                      return ("🟨")
                            
                    else:
                      return ("⬛️")
  
                def correct20():
                  if answer2[0] == wordle5[0]:
                    return ("🟩")
        
                  if answer2[0] != wordle5[0]:
                    if wordle5[0] in answer2:
                      return ("🟨")
                      
                    else:
                      return ("⬛️")
  
                def correct21():
                  if answer2[1] == wordle5[1]:
                    return ("🟩")
        
                  if answer2[1] != wordle5[1]:
                    if wordle5[1] in answer2:
                      return ("🟨")
                      
                    else:
                      return ("⬛️")
      
                def correct22():
                  if answer2[2] == wordle5[2]:
                    return ("🟩")
        
                  if answer2[2] != wordle5[2]:
                    if wordle5[2] in answer2:
                      return ("🟨")
                      
                    else:
                      return ("⬛️")
                
                def correct23():
                  if answer2[3] == wordle5[3]:
                    return ("🟩")
        
                  if answer2[3] != wordle5[3]:
                    if wordle5[3] in answer2:
                      return ("🟨")
                      
                    else:
                      return ("⬛️")
      
                def correct24():
                  if answer2[4] == wordle5[4]:
                    return ("🟩")
        
                  if answer2[4] != wordle5[4]:
                    if wordle5[4] in answer2:
                      return ("🟨")
                      
                    else:
                      return ("⬛️")
  
  
    
                print(" ")
                print("Wordle made by Tharun Dhanabal, 5/6")
                print(correct() + correct1() + correct2() + correct3() + correct4())
                print(correct5() + correct6() + correct7() + correct8() + correct9())
                print(correct10() + correct11() + correct12() + correct13() + correct14())
                print(correct15() + correct16() + correct17() + correct18() + correct19())
                print(correct20() + correct21() + correct22() + correct23() + correct24())
                break
  
    
              if askResults == "No" or askResults == "no":
                print(" ")
                print("Alright!")
                break
  
  
            
            if incorrect4 != answer2:
              os.system('clear')
              board5()
              incorrect5 = input(Fore.RED + "Incorrect" + Fore.WHITE + ". Last guess: ")
              incorrect5 = list(incorrect5)
    
              wordle6[0] = incorrect5[0]
              wordle6[1] = incorrect5[1]
              wordle6[2] = incorrect5[2]
              wordle6[3] = incorrect5[3]
              wordle6[4] = incorrect5[4]
  
              def corrections26():
                if answer2[0] == wordle6[0]:
                  return(Fore.LIGHTGREEN_EX + Style.BRIGHT + wordle6[0])
            
                if answer2[0] != wordle6[0]:
                  if wordle6[0] in answer2:
                    return(Fore.LIGHTYELLOW_EX + Style.BRIGHT + wordle6[0])
            
                  else:
                    return(colorama.Style.DIM + wordle6[0])
  
              def corrections27():
                if answer2[1] == wordle6[1]:
                  return(Fore.LIGHTGREEN_EX + Style.BRIGHT + wordle6[1])
            
                if answer2[1] != wordle6[1]:
                  if wordle6[1] in answer2:
                    return(Fore.LIGHTYELLOW_EX + Style.BRIGHT + wordle6[1])
            
                  else:
                    return(colorama.Style.DIM + wordle6[1])
          
              def corrections28():
                if answer2[2] == wordle6[2]:
                  return(Fore.LIGHTGREEN_EX + Style.BRIGHT + wordle6[2])
            
                if answer2[2] != wordle6[2]:
                  if wordle6[2] in answer2:
                    return(Fore.LIGHTYELLOW_EX + Style.BRIGHT + wordle6[2])
            
                  else:
                    return(colorama.Style.DIM + wordle6[2])
          
              def corrections29():
                if answer2[3] == wordle6[3]:
                  return(Fore.LIGHTGREEN_EX + Style.BRIGHT + wordle6[3])
            
                if answer2[3] != wordle6[3]:
                  if wordle6[3] in answer2:
                    return(Fore.LIGHTYELLOW_EX + Style.BRIGHT + wordle6[3])
            
                  else:
                    return(colorama.Style.DIM + wordle6[3])
          
              def corrections30():
                if answer2[4] == wordle6[4]:
                  return(Fore.LIGHTGREEN_EX + Style.BRIGHT + wordle6[4])
            
                if answer2[4] != wordle6[4]:
                  if wordle5[4] in answer2:
                    return(Fore.LIGHTYELLOW_EX + Style.BRIGHT + wordle6[4])
            
                  else:
                    return(colorama.Style.DIM + wordle6[4])


              def board6():
                print(Fore.LIGHTGREEN_EX +"W" + Fore.LIGHTYELLOW_EX + "o" + Style.DIM + Fore.WHITE + "r" + Style.NORMAL + Fore.LIGHTGREEN_EX + "d" + Fore.LIGHTYELLOW_EX + "l" + Style.DIM + Fore.WHITE + "e" + Style.NORMAL + Fore.WHITE + ":")
                print(corrections1() + Fore.WHITE + Style.NORMAL +  " | " + corrections2() + Fore.WHITE + Style.NORMAL + " | " + corrections3() + Fore.WHITE + Style.NORMAL + " | " + corrections4() + Fore.WHITE + Style.NORMAL + " | " + corrections5())
                print(corrections6() + Fore.WHITE + Style.NORMAL + " | " + corrections7() + Fore.WHITE + Style.NORMAL + " | " + corrections8() + Fore.WHITE + Style.NORMAL + " | " + corrections9() + Fore.WHITE + Style.NORMAL + " | " + corrections10())
                print(corrections11() + Fore.WHITE + Style.NORMAL + " | " + corrections12() + Fore.WHITE + Style.NORMAL + " | " + corrections13() + Fore.WHITE + Style.NORMAL + " | " + corrections14() + Fore.WHITE + Style.NORMAL + " | " + corrections15())
                print(corrections16() + Fore.WHITE + Style.NORMAL + " | " + corrections17() + Fore.WHITE + Style.NORMAL + " | " + corrections18() + Fore.WHITE + Style.NORMAL + " | " + corrections19() + Fore.WHITE + Style.NORMAL + " | " + corrections20())
                print(corrections21() + Fore.WHITE + Style.NORMAL + " | " + corrections22() + Fore.WHITE + Style.NORMAL + " | " + corrections23() + Fore.WHITE + Style.NORMAL + " | " + corrections24() + Fore.WHITE + Style.NORMAL + " | " + corrections25())
                print(corrections26() + Fore.WHITE + Style.NORMAL + " | " + corrections27() + Fore.WHITE + Style.NORMAL + " | " + corrections28() + Fore.WHITE + Style.NORMAL + " | " + corrections29() + Fore.WHITE + Style.NORMAL + " | " + corrections30())
                                                                                                                                                                                                                                             
            if incorrect5 == answer2: 
              os.system('clear')
              board6()
              print(Fore.LIGHTGREEN_EX + "Correct" + Fore.WHITE + ".")

              askResults = input("Would you like to print results?: ")
      
              if askResults == "Yes" or askResults == "yes":
                def correct():
                  if answer2[0] == wordle1[0]:
                    return ("🟩")
            
                  if answer2[0] != wordle1[0]:
                    if wordle1[0] in answer2:
                      return ("🟨")
                
                    else:
                      return ("⬛️")
        
                def correct1():
                  if answer2[1] == wordle1[1]:
                    return ("🟩")
                
                  if answer2[1] != wordle1[1]:
                    if wordle1[1] in answer2:
                      return ("🟨")
                
                    else:
                      return ("⬛️")
        
                def correct2():
                  if answer2[2] == wordle1[2]:
                    return ("🟩")
                
                  if answer2[2] != wordle1[2]:
                    if wordle1[2] in answer2:
                      return ("🟨")
                
                    else:
                      return ("⬛️")
        
                def correct3():
                  if answer2[3] == wordle1[3]:
                    return ("🟩")
                
                  if answer2[3] != wordle1[3]:
                    if wordle1[3] in answer2:
                      return ("🟨")
                
                    else:
                      return ("⬛️")
        
                def correct4():
                  if answer2[4] == wordle1[4]:
                    return ("🟩")
                
                  if answer2[4] != wordle1[4]:
                    if wordle1[4] in answer2:
                      return ("🟨")
                
                    else:
                      return ("⬛️")
      
                def correct5():
                  if answer2[0] == wordle2[0]:
                    return ("🟩")
                    
                
                  if answer2[0] != wordle2[0]:
                    if wordle2[0] in answer2:
                      return ("🟨")
                
                    else:
                      return ("⬛️")
                
                def correct6():
                  if answer2[1] == wordle2[1]:
                    return ("🟩")
                
                  if answer2[1] != wordle2[1]:
                    if wordle2[1] in answer2:
                      return ("🟨")
                
                    else:
                      return("⬛️")
                
                def correct7():
                  if answer2[2] == wordle2[2]:
                    return ("🟩")
                
                  if answer2[2] != wordle2[2]:
                    if wordle2[2] in answer2:
                      return ("🟨")
                
                    else:
                      return ("⬛️")
                
                def correct8():
                  if answer2[3] == wordle2[3]:
                    return ("🟩")
                
                  if answer2[3] != wordle2[3]:
                    if wordle2[3] in answer2:
                      return ("🟨")
                
                    else:
                      return ("⬛️")
                
                def correct9():
                  if answer2[4] == wordle2[4]:
                    return ("🟩")
                
                  if answer2[4] != wordle2[4]:
                    if wordle2[4] in answer2:
                      return ("🟨")
                
                    else: 
                      return ("⬛️")
    
                def correct10():
                  if answer2[0] == wordle3[0]:
                    return ("🟩")
                    
                
                  if answer2[0] != wordle3[0]:
                    if wordle3[0] in answer2: 
                      return ("🟨")
                
                    else:
                      return ("⬛️")
                
                def correct11():
                  if answer2[1] == wordle3[1]:
                    return ("🟩")
                
                  if answer2[1] != wordle3[1]:
                    if wordle3[1] in answer2:
                      return ("🟨")
                
                    else:
                      return ("⬛️")
          
                def correct12():
                  if answer2[2] == wordle3[2]:
                    return ("🟩")
          
                  if answer2[2] != wordle3[2]:
                    if wordle3[2] in answer2:
                      return ("🟨")
          
                    else:
                      return ("⬛️")
          
                def correct13():
                  if answer2[3] == wordle3[3]:
                    return ("🟩")
          
                  if answer2[3] != wordle3[3]:
                    if wordle3[3] in answer2:
                      return ("🟨")
          
                    else:
                      return ("⬛️")
          
                def correct14():
                  if answer2[4] == wordle3[4]:
                    return ("🟩")
          
                  if answer2[4] != wordle3[4]:
                    if wordle2[4] in answer2:
                      return ("🟨")
          
                    else: 
                      return ("⬛️")
  
                def correct15():
                  if answer2[0] == wordle4[0]:
                    return ("🟩")
                      
                  
                  if answer2[0] != wordle4[0]:
                    if wordle4[0] in answer2:
                      return ("🟨")
                  
                    else:
                      return ("⬛️")
                
                def correct16():
                  if answer2[1] == wordle4[1]:
                    return ("🟩")
                
                  if answer2[1] != wordle4[1]:
                    if wordle4[1] in answer2:
                      return ("🟨")
                
                    else:
                      return("⬛️")
                
                def correct17():
                  if answer2[2] == wordle4[2]:
                    return ("🟩")
                
                  if answer2[2] != wordle4[2]:
                    if wordle4[2] in answer2:
                      return ("🟨")
                
                    else:
                      return ("⬛️")
                
                def correct18():
                  if answer2[3] == wordle4[3]:
                    return("🟩")
                
                  if answer2[3] != wordle4[3]:
                    if wordle4[3] in answer2:
                      return ("🟨")
                
                    else:
                      return ("⬛️")
                
                def correct19():
                  if answer2[4] == wordle4[4]:
                    return ("🟩")
                
                  if answer2[4] != wordle4[4]:
                    if wordle4[4] in answer2:
                      return ("🟨")
                            
                    else:
                      return ("⬛️")
  
                def correct20():
                  if answer2[0] == wordle5[0]:
                    return ("🟩")
        
                  if answer2[0] != wordle5[0]:
                    if wordle5[0] in answer2:
                      return ("🟨")
                      
                    else:
                      return ("⬛️")
  
                def correct21():
                  if answer2[1] == wordle5[1]:
                    return ("🟩")
        
                  if answer2[1] != wordle5[1]:
                    if wordle5[1] in answer2:
                      return ("🟨")
                      
                    else:
                      return ("⬛️")
      
                def correct22():
                  if answer2[2] == wordle5[2]:
                    return ("🟩")
        
                  if answer2[2] != wordle5[2]:
                    if wordle5[2] in answer2:
                      return ("🟨")
                      
                    else:
                      return ("⬛️")
                
                def correct23():
                  if answer2[3] == wordle5[3]:
                    return ("🟩")
        
                  if answer2[3] != wordle5[3]:
                    if wordle5[3] in answer2:
                      return ("🟨")
                      
                    else:
                      return ("⬛️")
      
                def correct24():
                  if answer2[4] == wordle5[4]:
                    return ("🟩")
        
                  if answer2[4] != wordle5[4]:
                    if wordle5[4] in answer2:
                      return ("🟨")
                      
                    else:
                      return ("⬛️")

                def correct25():
                  if answer2[0] == wordle6[0]:
                    return ("🟩")
      
  
                  if answer2[0] != wordle6[0]:
                    if wordle5[0] in answer2:
                      return ("🟨")

                    else:
                      return ("⬛️")
                  
                def correct26():
                  if answer2[1] == wordle6[1]:
                    return ("🟩")
      
                  if answer2[1] != wordle6[1]:
                    if wordle6[1] in answer2:
                      return ("🟨")
    
                    else:
                      return ("⬛️")
    
                def correct27():
                  if answer2[2] == wordle6[2]:
                    return ("🟩")
      
                  if answer2[2] != wordle6[2]:
                    if wordle6[2] in answer2:
                      return ("🟨")
    
                    else:
                      return ("⬛️")
      
                def correct28():
                  if answer2[3] == wordle6[3]:
                    return ("🟩")
      
                  if answer2[3] != wordle6[3]:
                    if wordle6[3] in answer2:
                      return ("🟨")
    
                    else:
                      return ("⬛️")
    
                def correct29():
                  if answer2[4] == wordle6[4]:
                    return ("🟩")
      
                  if answer2[4] != wordle6[4]:
                    if wordle6[4] in answer2:
                      return ("🟨")
    
                    else:
                      return ("⬛️")
  
  
                print(" ")
                print("Wordle made by Tharun Dhanabal, 6/6")
                print(correct() + correct1() + correct2() + correct3() + correct4())
                print(correct5() + correct6() + correct7() + correct8() + correct9())
                print(correct10() + correct11() + correct12() + correct13() + correct14())
                print(correct15() + correct16() + correct17() + correct18() + correct19())
                print(correct20() + correct21() + correct22() + correct23() + correct24())
                print(correct25() + correct26() + correct27() + correct28() + correct29())
                break
  
    
              if askResults == "No" or askResults == "no":
                print(" ")
                print("Alright!")
                break
  
            if incorrect5 != answer2:
              os.system('clear')
              board6()
              answer2 = answer1
              print("Ahh shucks. The word was: " + Fore.LIGHTGREEN_EX + str(answer2) + Fore.WHITE + ".")

              askResults = input("Would you like to print results?: ")
      
              if askResults == "Yes" or askResults == "yes":
                def correct():
                  if answer2[0] == wordle1[0]:
                    return ("🟩")
            
                  if answer2[0] != wordle1[0]:
                    if wordle1[0] in answer2:
                      return ("🟨")
                
                    else:
                      return ("⬛️")
        
                def correct1():
                  if answer2[1] == wordle1[1]:
                    return ("🟩")
                
                  if answer2[1] != wordle1[1]:
                    if wordle1[1] in answer2:
                      return ("🟨")
                
                    else:
                      return ("⬛️")
        
                def correct2():
                  if answer2[2] == wordle1[2]:
                    return ("🟩")
                
                  if answer2[2] != wordle1[2]:
                    if wordle1[2] in answer2:
                      return ("🟨")
                
                    else:
                      return ("⬛️")
        
                def correct3():
                  if answer2[3] == wordle1[3]:
                    return ("🟩")
                
                  if answer2[3] != wordle1[3]:
                    if wordle1[3] in answer2:
                      return ("🟨")
                
                    else:
                      return ("⬛️")
        
                def correct4():
                  if answer2[4] == wordle1[4]:
                    return ("🟩")
                
                  if answer2[4] != wordle1[4]:
                    if wordle1[4] in answer2:
                      return ("🟨")
                
                    else:
                      return ("⬛️")
      
                def correct5():
                  if answer2[0] == wordle2[0]:
                    return ("🟩")
                    
                
                  if answer2[0] != wordle2[0]:
                    if wordle2[0] in answer2:
                      return ("🟨")
                
                    else:
                      return ("⬛️")
                
                def correct6():
                  if answer2[1] == wordle2[1]:
                    return ("🟩")
                
                  if answer2[1] != wordle2[1]:
                    if wordle2[1] in answer2:
                      return ("🟨")
                
                    else:
                      return("⬛️")
                
                def correct7():
                  if answer2[2] == wordle2[2]:
                    return ("🟩")
                
                  if answer2[2] != wordle2[2]:
                    if wordle2[2] in answer2:
                      return ("🟨")
                
                    else:
                      return ("⬛️")
                
                def correct8():
                  if answer2[3] == wordle2[3]:
                    return ("🟩")
                
                  if answer2[3] != wordle2[3]:
                    if wordle2[3] in answer2:
                      return ("🟨")
                
                    else:
                      return ("⬛️")
                
                def correct9():
                  if answer2[4] == wordle2[4]:
                    return ("🟩")
                
                  if answer2[4] != wordle2[4]:
                    if wordle2[4] in answer2:
                      return ("🟨")
                
                    else: 
                      return ("⬛️")
    
                def correct10():
                  if answer2[0] == wordle3[0]:
                    return ("🟩")
                    
                
                  if answer2[0] != wordle3[0]:
                    if wordle3[0] in answer2: 
                      return ("🟨")
                
                    else:
                      return ("⬛️")
                
                def correct11():
                  if answer2[1] == wordle3[1]:
                    return ("🟩")
                
                  if answer2[1] != wordle3[1]:
                    if wordle3[1] in answer2:
                      return ("🟨")
                
                    else:
                      return ("⬛️")
          
                def correct12():
                  if answer2[2] == wordle3[2]:
                    return ("🟩")
          
                  if answer2[2] != wordle3[2]:
                    if wordle3[2] in answer2:
                      return ("🟨")
          
                    else:
                      return ("⬛️")
          
                def correct13():
                  if answer2[3] == wordle3[3]:
                    return ("🟩")
          
                  if answer2[3] != wordle3[3]:
                    if wordle3[3] in answer2:
                      return ("🟨")
          
                    else:
                      return ("⬛️")
          
                def correct14():
                  if answer2[4] == wordle3[4]:
                    return ("🟩")
          
                  if answer2[4] != wordle3[4]:
                    if wordle2[4] in answer2:
                      return ("🟨")
          
                    else: 
                      return ("⬛️")
  
                def correct15():
                  if answer2[0] == wordle4[0]:
                    return ("🟩")
                      
                  
                  if answer2[0] != wordle4[0]:
                    if wordle4[0] in answer2:
                      return ("🟨")
                  
                    else:
                      return ("⬛️")
                
                def correct16():
                  if answer2[1] == wordle4[1]:
                    return ("🟩")
                
                  if answer2[1] != wordle4[1]:
                    if wordle4[1] in answer2:
                      return ("🟨")
                
                    else:
                      return("⬛️")
                
                def correct17():
                  if answer2[2] == wordle4[2]:
                    return ("🟩")
                
                  if answer2[2] != wordle4[2]:
                    if wordle4[2] in answer2:
                      return ("🟨")
                
                    else:
                      return ("⬛️")
                
                def correct18():
                  if answer2[3] == wordle4[3]:
                    return("🟩")
                
                  if answer2[3] != wordle4[3]:
                    if wordle4[3] in answer2:
                      return ("🟨")
                
                    else:
                      return ("⬛️")
                
                def correct19():
                  if answer2[4] == wordle4[4]:
                    return ("🟩")
                
                  if answer2[4] != wordle4[4]:
                    if wordle4[4] in answer2:
                      return ("🟨")
                            
                    else:
                      return ("⬛️")
  
                def correct20():
                  if answer2[0] == wordle5[0]:
                    return ("🟩")
        
                  if answer2[0] != wordle5[0]:
                    if wordle5[0] in answer2:
                      return ("🟨")
                      
                    else:
                      return ("⬛️")
  
                def correct21():
                  if answer2[1] == wordle5[1]:
                    return ("🟩")
        
                  if answer2[1] != wordle5[1]:
                    if wordle5[1] in answer2:
                      return ("🟨")
                      
                    else:
                      return ("⬛️")
      
                def correct22():
                  if answer2[2] == wordle5[2]:
                    return ("🟩")
        
                  if answer2[2] != wordle5[2]:
                    if wordle5[2] in answer2:
                      return ("🟨")
                      
                    else:
                      return ("⬛️")
                
                def correct23():
                  if answer2[3] == wordle5[3]:
                    return ("🟩")
        
                  if answer2[3] != wordle5[3]:
                    if wordle5[3] in answer2:
                      return ("🟨")
                      
                    else:
                      return ("⬛️")
      
                def correct24():
                  if answer2[4] == wordle5[4]:
                    return ("🟩")
        
                  if answer2[4] != wordle5[4]:
                    if wordle5[4] in answer2:
                      return ("🟨")
                      
                    else:
                      return ("⬛️")

                def correct25():
                  if answer2[0] == wordle6[0]:
                    return ("🟩")
      
  
                  if answer2[0] != wordle6[0]:
                    if wordle5[0] in answer2:
                      return ("🟨")

                    else:
                      return ("⬛️")
                  
                def correct26():
                  if answer2[1] == wordle6[1]:
                    return ("🟩")
      
                  if answer2[1] != wordle6[1]:
                    if wordle6[1] in answer2:
                      return ("🟨")
    
                    else:
                      return ("⬛️")
    
                def correct27():
                  if answer2[2] == wordle6[2]:
                    return ("🟩")
      
                  if answer2[2] != wordle6[2]:
                    if wordle6[2] in answer2:
                      return ("🟨")
    
                    else:
                      return ("⬛️")
      
                def correct28():
                  if answer2[3] == wordle6[3]:
                    return ("🟩")
      
                  if answer2[3] != wordle6[3]:
                    if wordle6[3] in answer2:
                      return ("🟨")
    
                    else:
                      return ("⬛️")
    
                def correct29():
                  if answer2[4] == wordle6[4]:
                    return ("🟩")
      
                  if answer2[4] != wordle6[4]:
                    if wordle6[4] in answer2:
                      return ("🟨")
    
                    else:
                      return ("⬛️")
  
  
                print(" ")
                print("Wordle made by Tharun Dhanabal, 6/6")
                print(correct() + correct1() + correct2() + correct3() + correct4())
                print(correct5() + correct6() + correct7() + correct8() + correct9())
                print(correct10() + correct11() + correct12() + correct13() + correct14())
                print(correct15() + correct16() + correct17() + correct18() + correct19())
                print(correct20() + correct21() + correct22() + correct23() + correct24())
                print(correct25() + correct26() + correct27() + correct28() + correct29())
                print("Sad :(")
                break
  
    
              if askResults == "No" or askResults == "no":
                print(" ")
                print("Alright!")
                print(" ")
                break

              
              


            
         

import colorama
from colorama import Fore
from colorama import Style 

print("Wordle Tutorial:")

print("Wordle is a game where you guess a 5-lettered word using 6 guesses based on these clues: ")
print(" ")
print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "W" + Fore.WHITE + " | "+ Style.DIM + "O" + Style.NORMAL + " | " + Style.DIM + "R" + Style.NORMAL + " | " + Style.DIM + "D" + Style.NORMAL + " | " + Fore.LIGHTYELLOW_EX + Style.BRIGHT + "S")

print(" ")
print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "W " + Style.NORMAL + Fore.WHITE + "= Means that the letter is in the word and is in the right spot")
print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "S " + Fore.WHITE + Style.NORMAL + "= Means that the letter in the word, but isn't in the right spot")
print(Style.DIM + "O" + Style.NORMAL + " | " + Style.DIM + "R" + Style.NORMAL + " | " + Style.DIM + "D " + Style.NORMAL + Fore.WHITE + "= Means that the letter isn't in the word and isn't in the right spot")

print(" ")

print("Enter a word: WORDS --> This is how to enter words into the prompt")

print(" ")

ENTER = input("If you understand, press " + Fore.LIGHTBLUE_EX + "[ENTER]")
import os 
os.system('clear')
wordle()

"""
Play the game also @: https://replit.com/@TharunDhanabal/Wordle?v=1

Here is my replit as well: https://replit.com/@TharunDhanabal
"""


#Created by Tharun Dhanabal in Python 3
#Vanilla version 0.10
