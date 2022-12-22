let fs = require('fs');

let lines = fs.readFileSync('C:\\Users\\Nahor Yirgaalem\\Projects\\Advent of Code\\Day4\\input.txt', 'utf8').toString()
.replace(/\r/g, "")
.split("\n")

pairs = 0
function part1(){
   
    for (let line of lines){
        left = []
        right = []
        split = line.split(",");
        l = split[0].split("-");
        r = split[1].split("-");
        
        left.push(parseInt(l[0]))
        left.push(parseInt(l[1]))
        right.push(parseInt(r[0]))
        right.push(parseInt(r[1]))
        //Check if the left side continas the left also if either are equal 
        if(left[0] <= right[0] && left[1] >= right[1])
            pairs++;
        // Check if the right side contains left
        else if(right[0] <= left[0] && right[1] >= left[1])
            pairs++;
        // console.log(pairs);
        
    }
    return pairs;
}

overlap = 0
function part2(){
    
    for (let line of lines){
        left = []
        right = []
        split = line.split(",");
        l = split[0].split("-");
        r = split[1].split("-");
        
        left.push(parseInt(l[0]));
        left.push(parseInt(l[1]));
        right.push(parseInt(r[0]));
        right.push(parseInt(r[1]));

        if (left[1] >= right[0] && left[0] <= right[0])
            overlap++;
        else if (right[1] >= left[0] && right[0] <= left[0])
            overlap++;

    }
    return overlap;
}

console.log(part1());
console.log(part2());