function encode(input){
    if (input.length==0) return "\"\"";
    let result="";
    var currentchar=input.charAt(0);
    var currentcharcount=1;
    var tempstr=""+currentchar;
    for (let i=1;i<input.length;i++){
        if (input.charAt(i)==currentchar){
            tempstr+=currentchar; currentcharcount+=1; continue;
        }
        if (currentcharcount>4) result+="/"+parseInt(currentcharcount/10)+(currentcharcount%10)+currentchar;
        else result+=tempstr;
        currentchar=input.charAt(i);
        currentcharcount=1;
        tempstr=""+currentchar;
    }
    if (currentcharcount>4)result+="/"+parseInt(currentcharcount/10)+(currentcharcount%10)+currentchar;
    else result+=tempstr;
    return result;
}
console.log(encode("aaaa"))
console.log(encode("aaaaa"))
console.log(encode(""))
console.log(encode("if(a){if(b){if(c){if(d){if(e){5 deeeeeeep}}}}}"))