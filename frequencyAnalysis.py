
#This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation
#Author: Srikanth Dabbiru
#Implement Frequency analysis taking the cipher & english alphabet frequencies as the input

ciphertext = """wbkgmodoxkiai jf mpl dls ulwpodawox wagplbadz yltawli gbjtly mj vl vjmp yaffawhxm ody xovjbajhi. ad mpl hdamly nadzyju, wbkgmodoxkmaw lffjbmi om vxlmwpxlk gobn yhbadz ighbbly mpl yltlxjguldm jf ujbl lffawaldm ulodi fjb wobbkadz jhm blglmamatl moini, ihwp oi uaxamobk wjyl vblonadz (ylwbkgmajd). mpai whxuadomly ad mpl yltlxjguldm jf mpl wjxjiihi, mpl sjbxy'i fabim fhxxk lxlwmbjdaw, yazamox, gbjzbouuovxl wjughmlb, spawp oiiaimly ad mpl ylwbkgmajd jf wagplbi zldlbomly vk mpl zlbuod obuk'i xjbldq iq40/42 uowpadl. lemldiatl jgld owoyluaw blilobwp admj wbkgmjzbogpk ai blxomatlxk blwldm, vlzaddadz ad mpl uay-1970i. ad mpl lobxk 1970i avu glbijddlx yliazdly mpl yomo ldwbkgmajd imodyoby (yli) oxzjbampu mpom vlwoul mpl fabim flylbox zjtlbduldm wbkgmjzbogpk imodyoby ad mpl hdamly imomli. ad 1976 spamfalxy yaffal ody uobmad plxxuod ghvxaiply mpl yaffalactplxxuod nlk lewpodzl oxzjbampu. ad 1977 mpl bio oxzjbampu soi ghvxaiply ad uobmad zobydlb'i iwaldmafaw oulbawod wjxhud. iadwl mpld, wbkgmjzbogpk poi vlwjul o saylxk hily mjjx ad wjuuhdawomajdi, wjughmlb dlmsjbni, ody wjughmlb ilwhbamk zldlboxxk."""

# source of frequency can be found in readme.md

class Analysis:
  def __init__(self): # constructor class
    self.alphabets = "abcdefghijklmnopqrstuvwxyz"
    self.frequency = {}
    self.alphafreq = {'a': 0.0817, 'b': 0.0150, 'c': 0.0278, 'd': 0.0425, 'e': 0.1270, 'f': 0.0223, 'g': 0.0202, 'h': 0.0609, 'i': 0.0697, 'j': 0.0015, 'k': 0.0077, 'l': 0.0403, 'm': 0.0241, 'n': 0.0675, 'o': 0.0751, 'p': 0.0193, 'q': 0.0010, 'r': 0.0599, 's': 0.0633, 't': 0.0906, 'u': 0.0276, 'v': 0.0098, 'w': 0.0236, 'x': 0.0015, 'y': 0.0197, 'z': 0.0007}
    
  def calculate_frequency(self, ciphertext): # calculate frequency method
    for char in self.alphabets:
      self.frequency[char] = 0
  
    textlength = 0
    for alphakey in ciphertext:
      if alphakey in self.frequency:
        self.frequency[alphakey] += 1
        textlength += 1

    for char in self.frequency:
      self.frequency[char] = round(self.frequency[char]/textlength, 4)

  def print_frequency(self): # print frequency
    line_count = 0
    for char in self.frequency:
      print(char, ':', self.frequency[char], ' ', end ='')
      if line_count % 3 == 2:
        print()
      line_count += 1
    print('\n')
    
  def compare_frequency(self):  # compare with original frequency
        self.mapping = mapping
        
         # Calculate closest matches based on the current state of mapping
        self.alphabets_filtered = {char: self.frequency[char] for char in self.alphabets if char not in self.mapping.keys()}
        closest_matches = {}
        for char in self.alphabets_filtered:
          closest_matches[char] = sorted(self.alphafreq.keys(), key=lambda x: abs(self.alphafreq[x] - self.frequency[char]))[:2]

        # Filter out values already defined in the mapping
        filtered_matches = {
            char: [match for match in matches if match not in self.mapping.values()]
            for char, matches in closest_matches.items()
        }

        # Calculate frequency for characters not yet mapped
        self.alphabets_filtered = {char: self.frequency[char] for char in self.alphabets if char not in self.mapping}

        # Print closest matches for characters not yet mapped
        for char in filtered_matches:
            print("Closest matches for", char, ":", filtered_matches[char])
        print('\n')
            
  def set_mapping(self, ciphertext, mapping):
        c_lines = ciphertext.split('. ') # Split each sentence by period
        m_lines = [''.join(mapping.get(c, c) for c in line) for line in c_lines]
        
        for c, m in zip(c_lines, m_lines):
            print("Cipher:", c.strip())
            print("Plains:", m.strip())
            print('\n')
      
analyse = Analysis()
analyse.calculate_frequency(ciphertext)
analyse.print_frequency()
# set mapping if able to analyse which ones are predictable 
mapping = {'l': 'e', 'm': 't', 'p': 'h', 'i': 's', 'a': 'i', 'd': 'n', 's': 'w', 'j': 'o', 'x': 'l', 'y': 'd', 'h': 'u', 'w': 'c', 'o': 'a', 'u': 'm', 'k': 'y', 'v': 'b', 'g': 'p', 'b': 'r', 'z': 'g', 'n': 'k', 't': 'v', 'e': 'x'}  # map alphabets until all are done and the resulting message is readable, konchem laborious mama but doable!
analyse.set_mapping(ciphertext, mapping)
analyse.compare_frequency()