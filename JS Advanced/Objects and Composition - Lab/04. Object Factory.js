function factory(library, orders){
    const result = [];

    for (let order of orders) {
        const device = Object.assign({}, order.template);

        for (let part of order.parts) {
            device[part] = library[part];
        }
        result.push(device);
    }
    return result;
}

