START{l=0;n=0;} {if(int($1)>l) n++; l=int($1);} END{print n-1}
