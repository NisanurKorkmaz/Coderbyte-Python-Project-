def CountingMinutes(str) {
  var time = str.split("-")
  var saat1 = time[0]
  var saat2 = time[1]

  def hesaplayici(s){
    
    saat=s.split(':');
    d=saat[1]
    dakika=d[0:2];
    ampm=d[2];
    toplamdakika=0;
    
    if ampm == 'am':
        pmdakika=720
    else :
        pmdakika=0
    

    toplamdakika=int(saat[0])*60 + int(dakika) + pmdakika ;

    return toplamdakika
  }
  
  sonuc=hesaplayici(saat2)-hesaplayici(saat1)

  if(sonuc<0){
    return (1440+sonuc)
  }
    
  else {
    return sonuc;
  }

}
   
// keep this function call here
console.log(CountingMinutes(readline()));
