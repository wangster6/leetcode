/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    var rtn = [...arr];
    for (let i = 0; i < arr.length; i++) {
        rtn[i] = fn(arr[i], i);
    }
    return rtn
};