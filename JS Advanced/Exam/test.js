const library = {
    calcPriceOfBook(nameOfBook, year) {

        let price = 20;
        if (typeof nameOfBook != "string" || !Number.isInteger(year)) {
            throw new Error("Invalid input");
        } else if (year <= 1980) {
            let total = price - (price * 0.5);
            return `Price of ${nameOfBook} is ${total.toFixed(2)}`;
        }
        return `Price of ${nameOfBook} is ${price.toFixed(2)}`;
    },

    findBook: function(booksArr, desiredBook) {
        if (booksArr.length == 0) {
            throw new Error("No books currently available");
        } else if (booksArr.find(e => e == desiredBook)) {
            return "We found the book you want.";
        } else {
            return "The book you are looking for is not here!";
        }

    },
    arrangeTheBooks(countBooks) {
        const countShelves = 5;
        const availableSpace = countShelves * 8;

        if (!Number.isInteger(countBooks) || countBooks < 0) {
            throw new Error("Invalid input");
        } else if (availableSpace >= countBooks) {
            return "Great job, the books are arranged.";
        } else {
            return "Insufficient space, more shelves need to be purchased.";
        }
    }

};



const { expect } = require('chai');


describe("Library", () => {
 
    describe("calcPriceOfBook", function () {

        it("defult price", () => {
            let library1 = library.calcPriceOfBook('Book', 1900);
            let expected = library1.price;
            expect(expected).to.be.undefined;
        });

        it("year less than 1980", () => {
            let expected = library.calcPriceOfBook('Book', 1900);
            expect(expected).equal('Price of Book is 10.00');
        });
        it("year above than 1980", () => {
            let expected = library.calcPriceOfBook('Book', 1990);
            expect(expected).equal('Price of Book is 20.00');
        });
        it("year exact 1980", () => {
            let expected = library.calcPriceOfBook('Book', 1980);
            expect(expected).equal('Price of Book is 10.00');
        });
        it("Invalid input", () => {
            expect( () => library.calcPriceOfBook(1, 1980)).to.throw("Invalid input");
            expect(() => library.calcPriceOfBook('Book', {})).to.throw("Invalid input");
            expect(() => library.calcPriceOfBook('Book', '1980')).to.throw("Invalid input");
            expect(() => library.calcPriceOfBook({}, [])).to.throw("Invalid input");
        });
 
    })
 
    describe("findBook", function () {
 
        it("Book is found", () => {
            let expected = library.findBook(['Book1', 'Book2'], 'Book1');
            expect(expected).equal('We found the book you want.');
        });
        it("Book not found", () => {
            let expected = library.findBook(['Book1', 'Book2'], 'Book3');
            expect(expected).equal('The book you are looking for is not here!');
        });
        it("Empty arr error", () => {
            expect(() => library.findBook([], 'Book1')).to.throw("No books currently available");

        });

    })
 
    describe("arrangeTheBooks", function () {

 
        it("Invalid input", () => {
            expect(() => library.arrangeTheBooks('Book1')).to.throw("Invalid input");
            expect(() => library.arrangeTheBooks({})).to.throw("Invalid input");
            expect(() => library.arrangeTheBooks(-5)).to.throw("Invalid input");

        });
        it("Enoght space", () => {
            let expected = library.arrangeTheBooks(40, 'Book');
            expect(expected).equal('Great job, the books are arranged.');
        });

        it("Zero books", () => {
            let expected = library.arrangeTheBooks(0, 'Book');
            expect(expected).equal('Great job, the books are arranged.');
        });

        it("Not enoght space", () => {
            let expected = library.arrangeTheBooks(50, 'Book');
            expect(expected).equal('Insufficient space, more shelves need to be purchased.');
        });
    })
})
