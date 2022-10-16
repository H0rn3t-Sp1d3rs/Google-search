from googlesearch import search

sex="""\033[1;32;36m
	|~| Coded By : H0rn3t Sp1d3rs |~|
	
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  
    [~] Github : https://github.com/h0rn3t-sp1d3rs
    [~] Page     : https://www.facebook.com/Bads.community.bd
    [~] Group    : https://www.facebook.com/groups/team.bads
  
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

           
"""
print(sex)


ok = str(input("\033[1;33;40m Enter Your Url:\033[1;35;40m "))

for i in search(ok, tld="co.in", num=5, stop=5, pause=2):
    print(i)

