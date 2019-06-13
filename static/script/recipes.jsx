class RecipeCard extends React.Component{
    state = { }
    componentDidMount(){
       

        //alert('calling the API to get videos for recipe ID ' + this.props.id);
        const instructionUrl = `https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/${this.props.id}/information`
        const videoUrl = `https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/videos/search?query=${this.props.title}&includeingredients=${this.props.query}`
        
        fetch(instructionUrl,
            {headers: {
                "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
                "X-RapidAPI-Key": "0fd28a9296msh61f75fee9171434p1d6995jsn9f02884e2ae5"
        }})
        .then(res => res.json())
        .then( result => {
             console.log("AAAAA===>", result)
            this.setState({ instruction:result.instructions});
        })


        fetch(videoUrl,
            {headers: {
                "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
                "X-RapidAPI-Key": "0fd28a9296msh61f75fee9171434p1d6995jsn9f02884e2ae5"
        }})
        .then(res => res.json())
        .then( result => {
             console.log("AAAAA===>", result)
            this.setState({ video:result.videos && result.videos.length && result.videos[0].youTubeId});
        })

        // ask for an individual recipes additional data
        // video search
        // instructions
    }
    render(){
       
        return (
            <div className="card" style={{width: "18rem", marginTop: "4rem"}}>
                <img className="card-img-top" style={{height: '300px'}} src={this.props.image} alt="Card image cap" />
                <div className="card-body">
                    <h5 className="card-title"> {this.props.title}</h5>
                    <p className="card-text"> {this.state.instruction?this.state.instruction.slice(0, 100) + "...": ""}</p>
                    <a href={"/recipes/" +this.props.id } className="btn btn-primary">Recipe Info</a>
                </div>
          
            {/* <div>
        <div>
            <img src={this.props.image}/>
           
        </div>
        {this.state.video && <iframe id="video" width="420" height="315" src={`https://www.youtube.com/embed/${this.state.video}`} frameborder="0" allowfullscreen></iframe>}
        <div> */}
            {/* {this.props.videos && this.props.videos.length && this.props.videos[0].youTubeId} */}
        {/* {this.props.videos && this.props.videos.length && <iframe id="video" width="420" height="315" src={`https://www.youtube.com/embed/${recipe.videos[0].youTubeId}`} frameborder="0" allowfullscreen></iframe>} */}
        {/* </div>
        <div>
             recipe title: {this.props.title}
        </div>


        <div>
            USED INGREDIENTS: 
            <IngredientList missing="False" ingredients={this.props.usedIngredients} />
        </div>
       
        <div>Missing Ingredients: </div>
            <IngredientList missing="True" ingredients={this.props.missedIngredients} />
        {this.props.instruction && <div>{this.props.instruction}</div>}
        
    </div>  */}
      </div>


        )
    }
}

class IngredientList extends React.Component{
   
   render(){
    let all_Ingredients =[];

    // for(let i = 0; i<this.state.recipes.ingredients; i++){
    //     // recipelist += this.state.recipes[i].title
    //     all_Ingredients.push(
        
    //      {ingredient: this.props.ingredient})
    // }
    console.log("====ingridents", this.props.ingredients)
    return (
        <div>{this.props.ingredients.map((ingredient)=> {

            return <div>
                <h1>{ingredient.name}</h1>
                <image src={ingredient.image}/>
                <div>{ingredient.amount}</div>
            </div>

        })}</div>
       )

   }
   
    

}



class Result extends React.Component{

    render(){
        const recipecards =[];
        for(const recipe of this.props.recipes){
            recipecards.push(
                <RecipeCard
                 recipe = {recipe}
                 ></RecipeCard>
            )
        }

        return(
            <div className="recipe">{RecipeCard}</div>
            
        )
    }
}


class SearchBar extends React.Component{

    render(){
       
        return(
            <form id="searchbar">
                <input 
                id="inputForsearchbar"
                placeholder="Search for ..."
                onChange={this.props.handlequerychange}
                value = {this.props.query}
                />
                <button onClick={this.props.handleSearch}  name="submit" className="btn btn-primary">Submit</button>
            </form>
            
        )
    }
}






class App extends React.Component {
    constructor(props){
        super(props);

        this.state ={
            query:'',
            recipes: [],
        }
         this.handleSearch = this.handleSearch.bind(this)
         this.handlequerychange=this.handlequerychange.bind(this)
    }

    handleSearch(evt){
        evt.preventDefault()

        
        const url =  window.location.search? "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients?number=5&ranking=1&ignorePantry=false&ingredients="
        : "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search?query="
        fetch(`${url}${this.state.query}`,
            {headers: {
                "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
                "X-RapidAPI-Key": "0fd28a9296msh61f75fee9171434p1d6995jsn9f02884e2ae5"
        }}).then(res => res.json())
         .then( result => {
             console.log("AAAAA", result)
        this.setState({ recipes:result.results? result.results: result});
         })
      }
    

    handlequerychange(evt){
        console.log(evt.target)
        console.log(evt.target.value)
        this.setState({
            query: evt.target.value
        })

    }

    render(){
        // loop over recipes
        // instatntiate a recipe card for each recipe from API like
        // <RecipeCard title={recipe.title} />
        let recipelist=[];

        for(let i = 0; i<this.state.recipes.length; i++){
            // recipelist += this.state.recipes[i].title
            recipelist.push(
            <RecipeCard
            
              title={this.state.recipes[i].title}
              id={this.state.recipes[i].id}
              query={this.state.query}
              name={this.state.recipes[i].name}
              usedIngredients={this.state.recipes[i].usedIngredients}
              missedIngredients={this.state.recipes[i].missedIngredients}
              image={this.state.recipes[i].image.includes('https')? this.state.recipes[i].image: "https://spoonacular.com/recipeImages/" + this.state.recipes[i].image} />);
             

        }

        return(
            <div>
             <SearchBar 
             handleSearch={this.handleSearch}
             handlequerychange={this.handlequerychange}
             query={this.state.query}
             />
            <div style={{
                display: "flex", 
                flexDirection: "row", 
                justifyContent: "space-between", 
                flexWrap:"wrap", 
                marginTop: "5rem",
                paddingLeft: "10rem",
                paddingRight: "10rem"}}>
            {recipelist}
            </div>

            </div>
            

            

        )
    }
}

ReactDOM.render(<App />, document.getElementById('root'));


