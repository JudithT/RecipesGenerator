import Recipes from './recipes'

class RecipeByRecipe extends React.Component {
    constructor(props){
        super(props);
    }

    render(){
        const url ="https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search?diet=vegetarian&excludeIngredients=coconut&intolerances=egg%2C+gluten&number=10&offset=0&type=main+course&query="

    
        return(  
            <Recipes url ={url} />    
        
        )
    }
}


ReactDOM.render(<RecipeByRecipe />, document.getElementById('root'));

    


 

