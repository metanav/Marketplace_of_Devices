import {generateRandomSubmodelValues} from './randomizer.js'


const  submodel = [
    {
        "idShort":"duration [min]",
        "modelType":"Property",
        "value":"",
        "valueType":"long",
        "semanticId":"0173-1#02-AAA818#006"
    },
    {
        "idShort":"maximum velocity at rated value [km/h]",
        "modelType":"Property",
        "value":"",
        "valueType":"long",
        "semanticId":"0173-1#02-AAB919#007"
    },
    {
        "idShort":"max. monitoring radius [m]",
        "modelType":"Property",
        "value":"",
        "valueType":"long",
        "semanticId":"0173-1#02-AAI957#004"
    },
    {
        "idShort":"2,4 GHz",
        "modelType":"Property",
        "value":"",
        "valueType":"boolean",
        "semanticId":"0173-1#07-ABA076#001"
    },
    {
        "idShort":"5 GHz",
        "modelType":"Property",
        "value":"",
        "valueType":"boolean",
        "semanticId":"0173-1#07-ABA075#001"
    },
    {
        "idShort":"energy consumption [kW/h]",
        "modelType":"Property",
        "value":"",
        "valueType":"decimal",
        "semanticId":"0173-1#02-AAF090#005"
    },
    {
        "idShort":"location [lat, lng]",
        "modelType":"Property",
        "value":"",
        "valueType":"string",
        "semanticId":"0173-1#02-BAF163#002"
    },
    {
        "idShort":"price",
        "modelType":"Property",
        "value":"",
        "valueType":"integer",
        "semanticId":"0173-1#02-AAO739#001"
    }
];

let datasets = {
    "duration [min]": [],
    "maximum velocity at rated value [km/h]": [],
    "max. monitoring radius [m]": [],
    "2,4 GHz": [],
    "5 GHz": [],
    "energy consumption [kW/h]": [],
    "location [lat, lng]": [],
    "price": []
  };

datasets = [];

for (let i = 0; i < 100; i++) {
    const generated_submodel =  generateRandomSubmodelValues(submodel);
    let  data =  {};
    for (let j  = 0; j < generated_submodel.length; j++) {
        const key   = generated_submodel[j]['idShort'];
        const value = generated_submodel[j]['value'];
        //datasets[key].push(value);
       data[key]  = value;
    }
    datasets.push(data);
}

console.log(JSON.stringify(datasets));
