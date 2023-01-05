/*

Create a function that takes an iterable (for example [1, 2, 1, 3, 1], [1, 2, 1, 3, 1, 2,2], [2, 1, 2, 1, 3, 1, 2])
and then returns the index of the most common element.
If the count of multiple elements is the same,
return the index of the first one.
 */

function test(elmnts){
    max=0;
    key='';
    commonElementCount = {};
    elmnts.forEach((elm)=>{
        commonElementCount[elm] = (commonElementCount[elm] || 0) +1;
        if(commonElementCount[elm]>max){
            max = commonElementCount[elm];
            key = elm;
        }
    });
    return elmnts.indexOf(key);
}
test([1, 2, 1, 3, 1])
test([1, 2, 1, 3, 1, 2,2])
test([2, 1, 2, 1, 3, 1, 2])
