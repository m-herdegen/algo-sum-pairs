exports.sumPairs = function(num_list, num) {
    ansArr = []

    for(i = 0; i < num_list.length; i++){
        for(j = 0; j < num_list.length; j++){
            if((num_list[i] + num_list[j] == num) && (i < j)){
                ansArr.push([num_list[i], num_list[j]])
            }
        }
    }
    if (ansArr.length == 0){
        return 'unable to find pairs'
    }
    
    return ansArr

};
console.log(exports.sumPairs([1,2,3,4,5], 9))
console.log(exports.sumPairs([1,2,3,4,5], 7))
console.log(exports.sumPairs([3, 1, 5, 8, 2], 27))