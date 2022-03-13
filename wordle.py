def wordle():
  answer = "today"
  #The word can change 
    
  wordle1 = ["-", "-", "-", "-", "-"]
  wordle2 = ["-", "-", "-", "-", "-"]
  wordle3 = ["-", "-", "-", "-", "-"]
  wordle4 = ["-", "-", "-", "-", "-"]
  wordle5 = ["-", "-", "-", "-", "-"]
  wordle6 = ["-", "-", "-", "-", "-"]

  
  print("Wordle: ")
  print(wordle1[0] + " "  + "|" + " " + wordle1[1] + " " + "|" + " " + wordle1[2] + " " + "|" + " " + wordle1[3] + " "  + "|" + " " + wordle1[4])
  print(wordle2[0] + " "  + "|" + " " + wordle2[1] + " " + "|" + " " + wordle2[2] + " " + "|" + " " + wordle2[3] + " "  + "|" + " " + wordle2[4])
  print(wordle3[0] + " "  + "|" + " " + wordle3[1] + " " + "|" + " " + wordle3[2] + " " + "|" + " " + wordle3[3] + " "  + "|" + " " + wordle3[4])
  print(wordle4[0] + " "  + "|" + " " + wordle4[1] + " " + "|" + " " + wordle4[2] + " " + "|" + " " + wordle4[3] + " "  + "|" + " " + wordle4[4])
  print(wordle5[0] + " "  + "|" + " " + wordle5[1] + " " + "|" + " " + wordle5[2] + " " + "|" + " " + wordle5[3] + " "  + "|" + " " + wordle5[4])
  print(wordle6[0] + " "  + "|" + " " + wordle6[1] + " " + "|" + " " + wordle6[2] + " " + "|" + " " + wordle6[3] + " "  + "|" + " " + wordle6[4])
  
        
  #first guess 
  prompt = input("Guess a word: ")
  prompt = list(prompt)
  answer = list(answer)

    
  wordle1[0] = prompt[0]
  wordle1[1] = prompt[1]
  wordle1[2] = prompt[2]
  wordle1[3] = prompt[3]
  wordle1[4] = prompt[4]

  
  def correct():
    if answer[0] == wordle1[0]:
      return ("🟢")
    

    if answer[0] != wordle1[0]:
      if wordle1[0] in answer:
        return ("🟡")

      else:
        return ("🔴")
#------------------------------
  def correct1():
    if answer[1] == wordle1[1]:
      return ("🟢")

    if answer[1] != wordle1[1]:
      if wordle1[1] in answer:
        return ("🟡")

      else:
        return ("🔴")
#------------------------------
  def correct2():
    if answer[2] == wordle1[2]:
      return ("🟢")

    if answer[2] != wordle1[2]:
      if wordle1[2] in answer:
        return ("🟡")

      else:
        return ("🔴")
#------------------------------
  def correct3():
    if answer[3] == wordle1[3]:
      return ("🟢")

    if answer[3] != wordle1[3]:
      if wordle1[3] in answer:
        return ("🟡")

      else:
        return ("🔴")
#------------------------------
  def correct4():
    if answer[4] == wordle1[4]:
      return ("🟢")

    if answer[4] != wordle1[4]:
      if wordle1[4] in answer:
        return ("🟡")

      else:
        return ("🔴")

    

  print(" ")
  print(wordle1[0] + " "  + "|" + " " + wordle1[1] + " " + "|" + " " + wordle1[2] + " " + "|" + " " + wordle1[3] + " "  + "|" + " " + wordle1[4] + " " + "-->" + " " + str(correct()) + ", " + str(correct1()) + ", " + str(correct2()) + ", " + str(correct3()) + ", " + str(correct4()))
  print(wordle2[0] + " "  + "|" + " " + wordle2[1] + " " + "|" + " " + wordle2[2] + " " + "|" + " " + wordle2[3] + " "  + "|" + " " + wordle2[4])
  print(wordle3[0] + " "  + "|" + " " + wordle3[1] + " " + "|" + " " + wordle3[2] + " " + "|" + " " + wordle3[3] + " "  + "|" + " " + wordle3[4])
  print(wordle4[0] + " "  + "|" + " " + wordle4[1] + " " + "|" + " " + wordle4[2] + " " + "|" + " " + wordle4[3] + " "  + "|" + " " + wordle4[4])
  print(wordle5[0] + " "  + "|" + " " + wordle5[1] + " " + "|" + " " + wordle5[2] + " " + "|" + " " + wordle5[3] + " "  + "|" + " " + wordle5[4])
  print(wordle6[0] + " "  + "|" + " " + wordle6[1] + " " + "|" + " " + wordle6[2] + " " + "|" + " " + wordle6[3] + " "  + "|" + " " + wordle6[4])
  
    
  if prompt == answer:
    print("Correct.")
  
  if prompt != answer:
    incorrect = input("Incorrect. Guess again: ")
    incorrect = list(incorrect)
      
    wordle2[0] = incorrect[0]
    wordle2[1] = incorrect[1]
    wordle2[2] = incorrect[2]
    wordle2[3] = incorrect[3]
    wordle2[4] = incorrect[4]

    def correct5():
      if answer[0] == wordle2[0]:
        return ("🟢")
    

      if answer[0] != wordle2[0]:
        if wordle2[0] in answer:
          return ("🟡")

        else:
          return ("🔴")
#--------------------------------
    def correct6():
      if answer[1] == wordle2[1]:
        return ("🟢")

      if answer[1] != wordle2[1]:
        if wordle2[1] in answer:
          return ("🟡")
#--------------------------------
    def correct7():
      if answer[2] == wordle2[2]:
        return ("🟢")

      if answer[2] != wordle2[2]:
        if wordle2[2] in answer:
          return ("🟡")

        else:
          return ("🔴")
#--------------------------------
    def correct8():
      if answer[3] == wordle2[3]:
        return ("🟢")

      if answer[3] != wordle2[3]:
        if wordle2[3] in answer:
          return ("🟡")

        else:
          return ("🔴")
#--------------------------------
    def correct9():
      if answer[4] == wordle2[4]:
        return ("🟢")

      if answer[4] != wordle2[4]:
        if wordle2[4] in answer:
          return ("🟡")

        else: 
          return ("🔴")
    
      
    print(" ")
    print(wordle1[0] + " "  + "|" + " " + wordle1[1] + " " + "|" + " " + wordle1[2] + " " + "|" + " " + wordle1[3] + " "  + "|" + " " + wordle1[4] + " " + "-->" + " " + str(correct()) + ", " + str(correct1()) + ", " + str(correct2()) + ", " + str(correct3()) + ", " + str(correct4()))
    print(wordle2[0] + " "  + "|" + " " + wordle2[1] + " " + "|" + " " + wordle2[2] + " " + "|" + " " + wordle2[3] + " "  + "|" + " " + wordle2[4] + " " + "-->" + " " + str(correct5()) + ", " + str(correct6()) + ", " + str(correct7()) + ", " + str(correct8()) + ", " + str(correct9()))
    print(wordle3[0] + " "  + "|" + " " + wordle3[1] + " " + "|" + " " + wordle3[2] + " " + "|" + " " + wordle3[3] + " "  + "|" + " " + wordle3[4])
    print(wordle4[0] + " "  + "|" + " " + wordle4[1] + " " + "|" + " " + wordle4[2] + " " + "|" + " " + wordle4[3] + " "  + "|" + " " + wordle4[4])
    print(wordle5[0] + " "  + "|" + " " + wordle5[1] + " " + "|" + " " + wordle5[2] + " " + "|" + " " + wordle5[3] + " "  + "|" + " " + wordle5[4])
    print(wordle6[0] + " "  + "|" + " " + wordle6[1] + " " + "|" + " " + wordle6[2] + " " + "|" + " " + wordle6[3] + " "  + "|" + " " + wordle6[4])
      
    if incorrect == answer:
      print("Correct.")
  
    if incorrect != answer:
      incorrect2 = input("Incorrect. Guess again: ")
      incorrect2 = list(incorrect2)
        
      wordle3[0] = incorrect2[0]
      wordle3[1] = incorrect2[1]
      wordle3[2] = incorrect2[2]
      wordle3[3] = incorrect2[3]
      wordle3[4] = incorrect2[4]

      def correct10():
        if answer[0] == wordle3[0]:
          return ("🟢")
    

        if answer[0] != wordle3[0]:
          if wordle3[0] in answer: 
            return ("🟡")

          else:
            return ("🔴")
#----------------------------------
      def correct11():
        if answer[1] == wordle3[1]:
          return ("🟢")

        if answer[1] != wordle3[1]:
          if wordle3[1] in answer:
            return ("🟡")

          else:
            return ("🔴")
#----------------------------------
      def correct12():
        if answer[2] == wordle3[2]:
          return ("🟢")

        if answer[2] != wordle3[2]:
          if wordle3[2] in answer:
            return ("🟡")

          else:
            return ("🔴")
#----------------------------------
      def correct13():
        if answer[3] == wordle3[3]:
          return ("🟢")

        if answer[3] != wordle3[3]:
          if wordle3[3] in answer:
            return ("🟡")

          else:
            return ("🔴")
#----------------------------------
      def correct14():
        if answer[4] == wordle3[4]:
          return ("🟢")

        if answer[4] != wordle3[4]:
          return ("🔴")
        
      print(" ")
      print(wordle1[0] + " "  + "|" + " " + wordle1[1] + " " + "|" + " " + wordle1[2] + " " + "|" + " " + wordle1[3] + " "  + "|" + " " + wordle1[4] + " " + "-->" + " " + str(correct()) + ", " + str(correct1()) + ", " + str(correct2()) + ", " + str(correct3()) + ", " + str(correct4()))
      print(wordle2[0] + " "  + "|" + " " + wordle2[1] + " " + "|" + " " + wordle2[2] + " " + "|" + " " + wordle2[3] + " "  + "|" + " " + wordle2[4] + " " + "-->" + " " + str(correct5()) + ", " + str(correct6()) + ", " + str(correct7()) + ", " + str(correct8()) + ", " + str(correct9()))
      print(wordle3[0] + " "  + "|" + " " + wordle3[1] + " " + "|" + " " + wordle3[2] + " " + "|" + " " + wordle3[3] + " "  + "|" + " " + wordle3[4] + " " + "-->" + " " + str(correct10()) + ", " + str(correct11()) + ", " + str(correct12()) + ", " + str(correct13()) + ", " + str(correct14()))
      print(wordle4[0] + " "  + "|" + " " + wordle4[1] + " " + "|" + " " + wordle4[2] + " " + "|" + " " + wordle4[3] + " "  + "|" + " " + wordle4[4])
      print(wordle5[0] + " "  + "|" + " " + wordle5[1] + " " + "|" + " " + wordle5[2] + " " + "|" + " " + wordle5[3] + " "  + "|" + " " + wordle5[4])
      print(wordle6[0] + " "  + "|" + " " + wordle6[1] + " " + "|" + " " + wordle6[2] + " " + "|" + " " + wordle6[3] + " "  + "|" + " " + wordle6[4])
      

      if incorrect2 == answer:
          print("Correct.")
  
      if incorrect2 != answer:
        incorrect3 = input("Incorrect. Guess again: ")
        incorrect3 = list(incorrect3)
  
        wordle4[0] = incorrect3[0]
        wordle4[1] = incorrect3[1]
        wordle4[2] = incorrect3[2]
        wordle4[3] = incorrect3[3]
        wordle4[4] = incorrect3[4]

        def correct15():
          if answer[0] == wordle4[0]:
            return ("🟢")
    

          if answer[0] != wordle4[0]:
            if wordle4 in answer:
              return ("🟡")

            else:
              return ("🔴")
#----------------------------------
        def correct16():
          if answer[1] == wordle4[1]:
            return ("🟢")

          if answer[1] != wordle4[1]:
            if wordle4[1] in answer:
              return ("🟡")

            else:
              return("🔴")
#----------------------------------
        def correct17():
          if answer[2] == wordle4[2]:
            return ("🟢")

          if answer[2] != wordle4[2]:
            if wordle4[2] in answer:
              return ("🟡")

            else:
              return ("🔴")
#----------------------------------
        def correct18():
          if answer[3] == wordle4[3]:
            return ("🟢")

          if answer[3] != wordle4[3]:
            if wordle4[3] in answer:
              return ("🟡")

            else:
              return ("🔴")
#----------------------------------
        def correct19():
          if answer[4] == wordle4[4]:
            return ("🟢")

          if answer[4] != wordle4[4]:
            if wordle4[4] in answer:
              return ("🟡")
            
            else:
              return ("🔴")
  
        print(" ")
        print(wordle1[0] + " "  + "|" + " " + wordle1[1] + " " + "|" + " " + wordle1[2] + " " + "|" + " " + wordle1[3] + " "  + "|" + " " + wordle1[4] + " " + "-->" + " " + str(correct()) + ", " + str(correct1()) + ", " + str(correct2()) + ", " + str(correct3()) + ", " + str(correct4()))
        print(wordle2[0] + " "  + "|" + " " + wordle2[1] + " " + "|" + " " + wordle2[2] + " " + "|" + " " + wordle2[3] + " "  + "|" + " " + wordle2[4] + " " + "-->" + " " + str(correct5()) + ", " + str(correct6()) + ", " + str(correct7()) + ", " + str(correct8()) + ", " + str(correct9()))
        print(wordle3[0] + " "  + "|" + " " + wordle3[1] + " " + "|" + " " + wordle3[2] + " " + "|" + " " + wordle3[3] + " "  + "|" + " " + wordle3[4] + " " + "-->" + " " + str(correct10()) + ", " + str(correct11()) + ", " + str(correct12()) + ", " + str(correct13()) + ", " + str(correct14()))
        print(wordle4[0] + " "  + "|" + " " + wordle4[1] + " " + "|" + " " + wordle4[2] + " " + "|" + " " + wordle4[3] + " "  + "|" + " " + wordle4[4] + " " + "-->" + " " + str(correct15()) + ", " + str(correct16()) + ", " + str(correct17()) + ", " + str(correct18()) + ", " + str(correct19()))
        print(wordle5[0] + " "  + "|" + " " + wordle5[1] + " " + "|" + " " + wordle5[2] + " " + "|" + " " + wordle5[3] + " "  + "|" + " " + wordle5[4])
        print(wordle6[0] + " "  + "|" + " " + wordle6[1] + " " + "|" + " " + wordle6[2] + " " + "|" + " " + wordle6[3] + " "  + "|" + " " + wordle6[4])
  
        if incorrect3 == answer:
          print("Correct.")
  
        if incorrect3 != answer:
          incorrect4 = input("Incorrect. Guess again: ")
          incorrect4 = list(incorrect4)
            
          wordle5[0] = incorrect4[0]
          wordle5[1] = incorrect4[1]
          wordle5[2] = incorrect4[2]
          wordle5[3] = incorrect4[3]
          wordle5[4] = incorrect4[4]
  
          def correct20():
            if answer[0] == wordle5[0]:
              return ("🟢")
  
            if answer[0] != wordle5[0]:
              if wordle5[0] in answer:
                return ("🟡")
                
              else:
                return ("🔴")
  #------------------------------------
          def correct21():
            if answer[1] == wordle5[1]:
              return ("🟢")
  
            if answer[1] != wordle5[1]:
              if wordle5[1] in answer:
                return ("🟡")
                
              else:
                return ("🔴")
  #------------------------------------
          def correct22():
            if answer[2] == wordle5[2]:
              return ("🟢")
  
            if answer[2] != wordle5[2]:
              if wordle5[2] in answer:
                return ("🟡")
                
              else:
                return ("🔴")
  #------------------------------------
          def correct23():
            if answer[3] == wordle5[3]:
              return ("🟢")
  
            if answer[3] != wordle5[3]:
              if wordle5[3] in answer:
                return ("🟡")
                
              else:
                return ("🔴")
  #------------------------------------
          def correct24():
            if answer[4] == wordle5[4]:
              return ("🟢")
  
            if answer[4] != wordle5[4]:
              if wordle5[4] in answer:
                return ("🟡")
                
              else:
                return ("🔴")
                
          print(" ")
          print(wordle1[0] + " "  + "|" + " " + wordle1[1] + " " + "|" + " " + wordle1[2] + " " + "|" + " " + wordle1[3] + " "  + "|" + " " + wordle1[4] + " " + "-->" + " " + str(correct()) + ", " + str(correct1()) + ", " + str(correct2()) + ", " + str(correct3()) + ", " + str(correct4()))
          print(wordle2[0] + " "  + "|" + " " + wordle2[1] + " " + "|" + " " + wordle2[2] + " " + "|" + " " + wordle2[3] + " "  + "|" + " " + wordle2[4] + " " + "-->" + " " + str(correct5()) + ", " + str(correct6()) + ", " + str(correct7()) + ", " + str(correct8()) + ", " + str(correct9()))
          print(wordle3[0] + " "  + "|" + " " + wordle3[1] + " " + "|" + " " + wordle3[2] + " " + "|" + " " + wordle3[3] + " "  + "|" + " " + wordle3[4] + " " + "-->" + " " + str(correct10()) + ", " + str(correct11()) + ", " + str(correct12()) + ", " + str(correct13()) + ", " + str(correct14()))
          print(wordle4[0] + " "  + "|" + " " + wordle4[1] + " " + "|" + " " + wordle4[2] + " " + "|" + " " + wordle4[3] + " "  + "|" + " " + wordle4[4] + " " + "-->" + " " + str(correct15()) + ", " + str(correct16()) + ", " + str(correct17()) + ", " + str(correct18()) + ", " + str(correct19()))
          print(wordle5[0] + " "  + "|" + " " + wordle5[1] + " " + "|" + " " + wordle5[2] + " " + "|" + " " + wordle5[3] + " "  + "|" + " " + wordle5[4] + " " + "-->" + " " + str(correct20()) + ", " + str(correct21()) + ", " + str(correct22()) + ", " + str(correct23()) + ", " + str(correct24()))
          print(wordle6[0] + " "  + "|" + " " + wordle6[1] + " " + "|" + " " + wordle6[2] + " " + "|" + " " + wordle6[3] + " "  + "|" + " " + wordle6[4])
  
          if incorrect4 == answer:
            print("Correct.")
    
          if incorrect4 != answer:
            incorrect5 = input("Incorrect. Last guess: ")
            incorrect5 = list(incorrect5)
  
            wordle6[0] = incorrect5[0]
            wordle6[1] = incorrect5[1]
            wordle6[2] = incorrect5[2]
            wordle6[3] = incorrect5[3]
            wordle6[4] = incorrect5[4]
  
            def correct25():
              if answer[0] == wordle5[0]:
                return ("🟢")
      
  
              if answer[0] != wordle5[0]:
                if wordle5[0] in answer:
                  return ("🟡")

                else:
                  return ("🔴")
  #-------------------------------------
            def correct26():
              if answer[1] == wordle5[1]:
                return ("🟢")
  
              if answer[1] != wordle5[1]:
                if wordle5[1] in answer:
                  return ("🟡")

                else:
                  return ("🔴")
  #-------------------------------------
            def correct27():
              if answer[2] == wordle5[2]:
                return ("🟢")
  
              if answer[2] != wordle5[2]:
                if wordle5[2] in answer:
                  return ("🟡")

                else:
                  return ("🔴")
  #-------------------------------------
            def correct28():
              if answer[3] == wordle5[3]:
                return ("🟢")
  
              if answer[3] != wordle5[3]:
                if wordle5[3] in answer:
                  return ("🟡")

                else:
                  return ("🔴")
  #-------------------------------------
            def correct29():
              if answer[4] == wordle5[4]:
                return ("🟢")
  
              if answer[4] != wordle5[4]:
                if wordle5[4] in answer:
                  return ("🟡")

                else:
                  return ("🔴")
    
            print(" ")
            print(wordle1[0] + " "  + "|" + " " + wordle1[1] + " " + "|" + " " + wordle1[2] + " " + "|" + " " + wordle1[3] + " "  + "|" + " " + wordle1[4] + " " + "-->" + " " + str(correct()) + ", " + str(correct1()) + ", " + str(correct2()) + ", " + str(correct3()) + ", " + str(correct4()))
            print(wordle2[0] + " "  + "|" + " " + wordle2[1] + " " + "|" + " " + wordle2[2] + " " + "|" + " " + wordle2[3] + " "  + "|" + " " + wordle2[4] + " " + "-->" + " " + str(correct5()) + ", " + str(correct6()) + ", " + str(correct7()) + ", " + str(correct8()) + ", " + str(correct9()))
            print(wordle3[0] + " "  + "|" + " " + wordle3[1] + " " + "|" + " " + wordle3[2] + " " + "|" + " " + wordle3[3] + " "  + "|" + " " + wordle3[4] + " " + "-->" + " " + str(correct10()) + ", " + str(correct11()) + ", " + str(correct12()) + ", " + str(correct13()) + ", " + str(correct14()))
            print(wordle4[0] + " "  + "|" + " " + wordle4[1] + " " + "|" + " " + wordle4[2] + " " + "|" + " " + wordle4[3] + " "  + "|" + " " + wordle4[4] + " " + "-->" + " " + str(correct15()) + ", " + str(correct16()) + ", " + str(correct17()) + ", " + str(correct18()) + ", " + str(correct19()))
            print(wordle5[0] + " "  + "|" + " " + wordle5[1] + " " + "|" + " " + wordle5[2] + " " + "|" + " " + wordle5[3] + " "  + "|" + " " + wordle5[4] + " " + "-->" + " " + str(correct20()) + ", " + str(correct21()) + ", " + str(correct22()) + ", " + str(correct23()) + ", " + str(correct24()))
            print(wordle6[0] + " "  + "|" + " " + wordle6[1] + " " + "|" + " " + wordle6[2] + " " + "|" + " " + wordle6[3] + " "  + "|" + " " + wordle6[4] + " " + "-->" + " " + str(correct25()) + ", " + str(correct26()) + ", " + str(correct27()) + ", " + str(correct28()) + ", " + str(correct29()))
                                                                                                                                                                                                                                                                 
            if incorrect5 == answer: 
              print("Correct.")
  
            if incorrect5 != answer:
              answer = "words"
              print("Ahh shucks. The word was: " + str(answer))

            

         
#Created by Tharun Dhanabal in Python 3
#Vanilla version 0.03

wordle()

  
  
  
