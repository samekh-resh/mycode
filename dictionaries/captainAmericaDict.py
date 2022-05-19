#!/usr/bin/env python3

CaptainAmerica ={ 'Real Name':'Steven Rogers','First Appearance':'Captain America Comics #1 (March, 1941)','Creators':['Joe Simon','Jack Kirby'],'Team Affiliations':'Avengers','Alias':'Winghead'}


realName = CaptainAmerica["Real Name"]
firstAppear = CaptainAmerica["First Appearance"]
famousCreator = CaptainAmerica["Creators"][1]
alias = CaptainAmerica["Alias"]

def main():
    print(f"{famousCreator} created Captain America, his real name being {realName}. he first appeared in the comic {firstAppear}. Funny this, his alias is {alias} ")




main()


