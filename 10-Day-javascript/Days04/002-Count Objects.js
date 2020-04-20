function getCount(objects) {
    var count = 0
    var n = Object.keys(objects).length
    for (var i = 0; i < n; i++) {

        if (objects[i].x == objects[i].y) {
            count = count + 1;
        }
    }
    return count
}