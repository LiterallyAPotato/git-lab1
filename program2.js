/*Program takes one or multiple strings and outputs all 
words which have duplicates. A word is indicated by a 
sequence of characters separated by whitespace. Comparisons are done insensitive to 
case, but output maintains the case of the first word. 
*/



let wordList = []
let words = new Map()
let firstOccurance = new Map()

if (process.argv.length <= 2){
    console.log("ERROR: You must provide at least one string")
    process.exit(-1)
}

for (let i = 2; i < process.argv.length; ++i) {
    for (j of process.argv[i].split(" ")){
        wordList.push(j.replace(/[^a-zA-Z ]/, ""))
    }
    //format the words into an array, remove all special characters
}

for (x of wordList){
    value = words.get(x.toLowerCase())
    if (value == undefined){
        //havent seen x before
        words.set(x.toLowerCase(), 1)
        firstOccurance.set(x.toLowerCase(), x)
    }else{
        words.set(x.toLowerCase(),value+1)
    }
    //if we have not seen a word before, 
    //add it to the words as lowercase
    //also add its first occurance as its original case
    //if we have seen a word, increment the counter
}

for(x of words.keys()){
    if (words.get(x) > 1){
        console.log(firstOccurance.get(x))
    }
}