//Realiza un programa que reciba el 
// siguiente objeto, e imprima otro 
// objeto con los siguientes datos:


const student = {
	name: "John Doe",
	grades: [
		{name: "math",grade: 80},
		{name: "science",grade: 100},
		{name: "history",grade: 60},
		{name: "PE",grade: 90},
		{name: "music",grade: 98}
	]
}

let total = 0;
let highest = student.grades[0];
let lowest = student.grades[0];

for(const subject of student.grades){
    total += subject.grade;
    if(subject.grade > highest.grade){
        highest = subject;
    };
    if (subject.grade < lowest.grade) {
        lowest = subject;
    };
};

const result = {
    name: student.name,
    gradeAvg: total / student.grades.length,
    highesGrade: highest.name,
    lowestGrade: lowest.name
}

console.log(result);