class SummerCamp {
    constructor(organizer, location) {
        this.organizer = organizer;
        this.location = location;
        this.priceForTheCamp = {"child": 150,
                                "student": 300,
                                "collegian": 500}
        this.listOfParticipants = [];
    }

    registerParticipant(name, condition, money) {
        const listOfCondition = Object.keys(this.priceForTheCamp);
        if (!listOfCondition.some(s => s == condition)) {
            throw new Error("Unsuccessful registration at the camp.");
        }
        if (this.listOfParticipants.some(s => s.name == name)) {
            return `The ${name} is already registered at the camp.`;
        }

        if (money < this.priceForTheCamp[condition]) {
            return `The money is not enough to pay the stay at the camp.`;
        } else {
            
            let participant = {
                'name': name,
                'condition': condition,
                'power': 100,
                'wins': 0
            }
            this.listOfParticipants.push(participant);
            return `The ${name} was successfully registered.`;
        }
    }

    unregisterParticipant(name) {
        if (!this.listOfParticipants.some(s => s.name == name)) {
            throw new Error(`The ${name} is not registered in the camp.`);
        }
        let participant = this.listOfParticipants.filter((p)=> p.name == name);
        const index = this.listOfParticipants.indexOf(participant);
        this.listOfParticipants.splice(index, 1);
        return `The ${name} removed successfully.`;
    }

    timeToPlay(typeOfGame, participant1, participant2) {
        const Par1 = this.listOfParticipants.find(p => p.name == participant1); 
        const Par2 = this.listOfParticipants.find(p => p.name == participant2);
        if (Par1 == undefined) {
            throw new Error(`Invalid entered name/s.`);
        }
        if (typeOfGame == 'WaterBalloonFights') {
            if (Par2 == undefined) {
                throw new Error(`Invalid entered name/s.`);
            }
            if (Par1.condition != Par2.condition) {
                throw new Error(`Choose players with equal condition.`);
            }
            if ( Par1.power > Par2.power) {
                Par1.wins += 1;
                return `The ${Par1.name} is winner in the game ${typeOfGame}.`
            } else if ( Par1.power < Par2.power) {
                Par2.wins += 1;
                return `The ${Par2.name} is winner in the game ${typeOfGame}.`
            } else {
                return `There is no winner.`
            }
        } else {
            Par1.power += 20;
            return `The ${participant1} successfully completed the game ${typeOfGame}.`;
        }
        

    }

    toString() {
        let result = [`${this.organizer} will take ${this.listOfParticipants.length} participants on camping to ${this.location}`]
        this.listOfParticipants
                .sort((a, b) => (b.wins - a.wins))
                .forEach(p => result
                .push(`${p.name} - ${p.condition} - ${p.power} - ${p.wins}`));
        return result.join('\n');
    }
}


const summerCamp = new SummerCamp("Jane Austen", "Pancharevo Sofia 1137, Bulgaria");
console.log(summerCamp.registerParticipant("Petar Petarson", "student", 200));
console.log(summerCamp.registerParticipant("Petar Petarson", "student", 300));
console.log(summerCamp.registerParticipant("Petar Petarson", "student", 300));
console.log(summerCamp.registerParticipant("Leila Wolfe", "childd", 200));

console.log('Input 2');

const summerCamp2 = new SummerCamp("Jane Austen", "Pancharevo Sofia 1137, Bulgaria");
console.log(summerCamp2.registerParticipant("Petar Petarson", "student", 300));
console.log(summerCamp2.unregisterParticipant("Petar"));
console.log(summerCamp2.unregisterParticipant("Petar Petarson"));


const summerCamp3 = new SummerCamp("Jane Austen", "Pancharevo Sofia 1137, Bulgaria");
console.log(summerCamp3.registerParticipant("Petar Petarson", "student", 300));
console.log(summerCamp3.timeToPlay("Battleship", "Petar Petarson"));
console.log(summerCamp3.registerParticipant("Sara Dickinson", "child", 200));
console.log(summerCamp3.timeToPlay("WaterBalloonFights", "Petar Petarson", "Sara Dickinson"));
console.log(summerCamp3.registerParticipant("Dimitur Kostov", "student", 300));
console.log(summerCamp3.timeToPlay("WaterBalloonFights", "Petar Petarson", "Dimitur Kostov"));


const summerCamp4 = new SummerCamp("Jane Austen", "Pancharevo Sofia 1137, Bulgaria");
console.log(summerCamp4.registerParticipant("Petar Petarson", "student", 300));
console.log(summerCamp4.timeToPlay("Battleship", "Petar Petarson"));
console.log(summerCamp4.registerParticipant("Sara Dickinson", "child", 200));
// console.log(summerCamp4.timeToPlay("WaterBalloonFights", "Petar Petarson", "Sara Dickinson"));
console.log(summerCamp4.registerParticipant("Dimitur Kostov", "student", 300));
console.log(summerCamp4.timeToPlay("WaterBalloonFights", "Petar Petarson", "Dimitur Kostov"));

console.log(summerCamp4.toString());

