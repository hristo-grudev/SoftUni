class List {
    _size;
    constructor() {
        this.colection = [];
        this.size = 0
    }
    add(el) {
        this.colection.push(el);
        this.colection.sort((a, b) => a - b);
        this.size++;
    };
    remove(index) {
        if (index >= 0 && index <= this.colection.length - 1) {
            this.colection.splice(index, 1);
            this.colection.sort((a, b) => a - b);
            this.size--;
        }
    }
    get(index) {
        if (index >= 0 && index <= this.colection.length - 1) {
            return this.colection[index];
        }
    }
}