function nbOccurences (list, searchElement) {
  this.list = list;
  this.searchElement = searchElement;
}

nbOccurences.prototype.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count += 1;
    }
  }
  return count;
};
module.exports = nbOccurences.prototype;
