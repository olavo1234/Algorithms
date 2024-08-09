const data = new Date()
const data2 = new Date('may 2007 3')
const data3 = new Date(2007,4,3)

console.log(data)
console.log(data2)
console.log(data3)

console.log(data2.toDateString())
console.log(data2.toTimeString())
console.log(data2.toISOString())
