def clean_list(list_to_clean):
    i = 0
    j = 1
    while i < len(list_to_clean):
        tmp = list_to_clean[i]
        while j < len(list_to_clean):
            
                if (tmp == list_to_clean[j])and(type(tmp) == type(list_to_clean[j])):
                    del list_to_clean[j]
                else:
                    j = j + 1
                
        
        i = i + 1
        j = i + 1
            
    return list_to_clean            
        
        

clean_list(['qwe', 'reg', 'qwe', 'REG'])
