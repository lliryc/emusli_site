
function MixViewModel()
{
    var self = this;
    self.food_categories_filter = [
            {name:'вегетерианские', id:'1', src: '/static/images/vegan-filter.svg'},
            {name:'без сахара', id:'2', src: '/static/images/sugarfree-filter.svg'},
            {name:'с протеином', id:'3', src: '/static/images/protein-filter.svg'},
            {name:'без лактозы', id:'4', src: '/static/images/lactosefree-filter.svg'},
            {name:'c клетчаткой', id:'5', src: '/static/images/highfibre-filter.svg'},
            {name: 'низкокалорийные', id:'6', src:'/static/images/lowfat-filter.svg'},
    ];

    self.cart = {
        base: [{id: '1', name:'name', ico_url: 'http://', qty: '1', portion: '100', price: '100', taste: 'sour'}],
        addition: [{id:'1', name:'name', ico_url: 'http://', qty: '1', portion: '100', price: '100', taste: 'sour'}],
        fruits: [{id:'1', name:'name', ico_url: 'http://', qty: '1', portion: '100', price: '100', taste: 'sour'}],
        nuts_seeds: [{id:'1', name:'name', img_url: 'http://', qty: '1', portion: '100', price: '100', taste: 'sour'}],
        choco: [{id:'1', name:'name', img_url: 'http://', qty: '1', portion: '100', price: '100', taste: 'sour'}],
    };

    self.food_catalog = {
        base:[
            {id:'1', name: 'name', img_url: 'img_url', ico_url: 'ico_url', short_desc:'short_desc', desc: 'desc',
            qty:'1', portion:'100', price:'100', new:'new'},
        ],
        addition:[
            {id:'1', name: 'name', img_url: 'img_url', ico_url: 'ico_url', short_desc:'short_desc', desc: 'desc',
            qty:'1', portion:'100', price:'100', new:'new'},
        ],
        fruits:[
            {id:'1', name: 'name', img_url: 'img_url', ico_url: 'ico_url', short_desc:'short_desc', desc: 'desc',
            qty:'1', portion:'100', price:'100', new:'new'},
        ],
        nuts_seeds:[
            {id:'1', name: 'name', img_url: 'img_url', ico_url: 'ico_url', short_desc:'short_desc', desc: 'desc',
            qty:'1', portion:'100', price:'100', new:'new'},
        ],
        choco:[
            {id:'1', name: 'name', img_url: 'img_url', ico_url: 'ico_url', short_desc:'short_desc', desc: 'desc',
            qty:'1', portion:'100', price:'100', new:'new'},
        ],

    };
}



}
