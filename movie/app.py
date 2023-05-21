# import numpy as np
# import pandas as pd
# import warnings


# warnings.filterwarnings('ignore')

# coln=["user_id","movie_id","rating","timestamp"]
# df=pd.read_csv("ml-100k/u.data",sep='\t',names=coln)

# df.head()

# df.shape

# df["user_id"].nunique()

# df["movie_id"].nunique()

# movie_title=pd.read_csv("ml-100k/u.item",sep='\|',header=None, encoding='latin1')

# movie_title[1].nunique()

# movie_title=movie_title[[0,1]]

# movie_title.columns=['movie_id','title']

# movie_title.head()

# df=pd.merge(df,movie_title,on="movie_id")

# df.tail()

# df.head()

# ##Exploratory Data Ananlysis

# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set_style('white')

# df

# df.groupby('title').mean()['rating'].sort_values(ascending=False).head()

# df.groupby('title').count()['rating'].sort_values(ascending=False)

# ratings=pd.DataFrame(df.groupby( 'title').mean()['rating'])

# ratings.head()

# ratings['no. of ratings']= pd.DataFrame(df.groupby('title').count()['rating'])

# ratings.sort_values(by='rating',ascending=False) 

# plt.figure(figsize=(10,6))
# plt.hist(ratings['no. of ratings'],bins=70)
# #plt.show()

# plt.hist(ratings['rating'],bins=70)
# #plt.show()

# sns.jointplot(x='rating',y='no. of ratings',data=ratings,alpha=0.5)

# ##Creating Movie Recommendation

# df.head()

# moviemat=df.pivot_table(index="user_id",columns="title",values="rating") 

# ratings.sort_values('no. of ratings',ascending=False)

# starwars_user_ratings=moviemat['Star Wars (1977)']
# starwars_user_ratings.head()

# similar_to_starwars=moviemat.corrwith(starwars_user_ratings)

# corr_starwars=pd.DataFrame(similar_to_starwars,columns=['Correlation'])

# corr_starwars

# corr_starwars.dropna(inplace=True)


# corr_starwars

# corr_starwars.sort_values('Correlation',ascending=False).head(10)

# corr_starwars


# ratings

# corr_starwars=corr_starwars.join(ratings['no. of ratings'])


# corr_starwars[corr_starwars['no. of ratings']>100].sort_values('Correlation',ascending=False)

# ##Predict Function

# def predict_movies(movie_name):
#     movie_user_ratings=moviemat[movie_name]  
#     similar_to_movie=moviemat.corrwith(movie_user_ratings)
#     corr_movie=pd.DataFrame(similar_to_movie,columns=['Correlation'])
#     corr_movie.dropna(inplace=True)
#     corr_movie=corr_movie.join(ratings['no. of ratings'])
#     predictions=corr_movie[corr_movie['no. of ratings']>100].sort_values('Correlation',ascending=False)

#     return predictions.head()





# from flask import Flask, render_template, request
# app=Flask(__name__,template_folder='template')
# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/recommend', methods=['POST'])
# def recommend_movies():
#     movie_name = request.form['movie_name']
#     predictions = predict_movies(movie_name)
#     return render_template('recommendations.html', movie_name=movie_name, predictions=predictions)

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request
# import numpy as np
# import pandas as pd
# import warnings

# warnings.filterwarnings('ignore')

# coln = ["user_id", "movie_id", "rating", "timestamp"]
# df = pd.read_csv("ml-100k/u.data", sep='\t', names=coln)

# movie_title = pd.read_csv("ml-100k/u.item", sep='|', header=None, encoding='latin1')
# movie_title = movie_title[[0, 1]]
# movie_title.columns = ['movie_id', 'title']

# df = pd.merge(df, movie_title, on="movie_id")

# moviemat = df.pivot_table(index="user_id", columns="title", values="rating")
# ratings = pd.DataFrame(df.groupby('title').mean()['rating'])
# ratings['no_of_ratings'] = pd.DataFrame(df.groupby('title').count()['rating'])
# corr_starwars = moviemat.corrwith(moviemat['Star Wars (1977)'])
# corr_starwars = pd.DataFrame(corr_starwars, columns=['Correlation'])
# corr_starwars.dropna(inplace=True)
# corr_starwars = corr_starwars.join(ratings['no_of_ratings'])
# corr_starwars = corr_starwars[corr_starwars['no_of_ratings'] > 100].sort_values('Correlation', ascending=False)

# app = Flask(__name__, template_folder='template')

# @app.route('/')
# def home():
#     return render_template('index.html', movie_titles=movie_title['title'])

# @app.route('/recommend', methods=['POST'])
# def recommend_movies():
#     movie_name = request.form['movie_name']
#     predictions = predict_movies(movie_name)
#     return render_template('recommendations.html', movie_name=movie_name, predictions=predictions)

# def predict_movies(movie_name):
#     movie_user_ratings = moviemat[movie_name]  
#     similar_to_movie = moviemat.corrwith(movie_user_ratings)
#     corr_movie = pd.DataFrame(similar_to_movie, columns=['Correlation'])
#     corr_movie.dropna(inplace=True)
#     corr_movie = corr_movie.join(ratings['no_of_ratings'])
#     predictions = corr_movie[corr_movie['no_of_ratings'] > 100].sort_values('Correlation', ascending=False)
#     return predictions.head()

# if __name__ == '__main__':
#     app.run(debug=True)




# from flask import Flask, render_template, request
# import numpy as np
# import pandas as pd
# import warnings

# warnings.filterwarnings('ignore')

# coln = ["user_id", "movie_id", "rating", "timestamp"]
# df = pd.read_csv("ml-100k/u.data", sep='\t', names=coln)

# movie_title = pd.read_csv("ml-100k/u.item", sep='|', header=None, encoding='latin1')
# movie_title = movie_title[[0, 1]]
# movie_title.columns = ['movie_id', 'title']

# df = pd.merge(df, movie_title, on="movie_id")

# moviemat = df.pivot_table(index="user_id", columns="title", values="rating")
# ratings = pd.DataFrame(df.groupby('title').mean()['rating'])
# ratings['no_of_ratings'] = pd.DataFrame(df.groupby('title').count()['rating'])
# corr_starwars = moviemat.corrwith(moviemat['Star Wars (1977)'])
# corr_starwars = pd.DataFrame(corr_starwars, columns=['Correlation'])
# corr_starwars.dropna(inplace=True)
# corr_starwars = corr_starwars.join(ratings['no_of_ratings'])
# corr_starwars = corr_starwars[corr_starwars['no_of_ratings'] > 100].sort_values('Correlation', ascending=False)

# app = Flask(__name__, template_folder='template')

# @app.route('/')
# def home():
#     return render_template('index.html', movie_titles=movie_title['title'])

# @app.route('/recommend', methods=['POST'])
# def recommend_movies():
#     movie_name = request.form['movie_name']
#     predictions = predict_movies(movie_name)
#     movie_titles = movie_title['title'].tolist()  # Get movie titles as a list
#     return render_template('recommendations.html', movie_name=movie_name, predictions=predictions, movie_titles=movie_titles)

# def predict_movies(movie_name):
#     movie_user_ratings = moviemat[movie_name]  
#     similar_to_movie = moviemat.corrwith(movie_user_ratings)
#     corr_movie = pd.DataFrame(similar_to_movie, columns=['Correlation'])
#     corr_movie.dropna(inplace=True)
#     corr_movie = corr_movie.join(ratings['no_of_ratings'])
#     predictions = corr_movie[corr_movie['no_of_ratings'] > 100].sort_values('Correlation', ascending=False)
#     return predictions.head()

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

coln = ["user_id", "movie_id", "rating", "timestamp"]
df = pd.read_csv("ml-100k/u.data", sep='\t', names=coln)

movie_title = pd.read_csv("ml-100k/u.item", sep='|', header=None, encoding='latin1')
movie_title = movie_title[[0, 1]]
movie_title.columns = ['movie_id', 'title']

df = pd.merge(df, movie_title, on="movie_id")

moviemat = df.pivot_table(index="user_id", columns="title", values="rating")
ratings = pd.DataFrame(df.groupby('title').mean()['rating'])
ratings['no_of_ratings'] = pd.DataFrame(df.groupby('title').count()['rating'])
corr_starwars = moviemat.corrwith(moviemat['Star Wars (1977)'])
corr_starwars = pd.DataFrame(corr_starwars, columns=['Correlation'])
corr_starwars.dropna(inplace=True)
corr_starwars = corr_starwars.join(ratings['no_of_ratings'])
corr_starwars = corr_starwars[corr_starwars['no_of_ratings'] > 100].sort_values('Correlation', ascending=False)

app = Flask(__name__, template_folder='template')

@app.route('/')
def home():
    return render_template('index.html', movie_titles=movie_title['title'])

@app.route('/recommend', methods=['POST'])
def recommend_movies():
    movie_name = request.form['movie_name']
    predictions = predict_movies(movie_name)
    return render_template('recommendations.html', movie_name=movie_name, predictions=predictions)

def predict_movies(movie_name):
    movie_user_ratings = moviemat[movie_name]  
    similar_to_movie = moviemat.corrwith(movie_user_ratings)
    corr_movie = pd.DataFrame(similar_to_movie, columns=['Correlation'])
    corr_movie.dropna(inplace=True)
    corr_movie = corr_movie.join(ratings['no_of_ratings'])
    predictions = corr_movie[corr_movie['no_of_ratings'] > 100].sort_values('Correlation', ascending=False)
    return predictions.head()

if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask, render_template, request
# import numpy as np
# import pandas as pd
# import warnings

# warnings.filterwarnings('ignore')

# coln = ["user_id", "movie_id", "rating", "timestamp"]
# df = pd.read_csv("ml-100k/u.data", sep='\t', names=coln)

# movie_title = pd.read_csv("ml-100k/u.item", sep='|', header=None, encoding='latin1')
# movie_title = movie_title[[0, 1]]
# movie_title.columns = ['movie_id', 'title']

# df = pd.merge(df, movie_title, on="movie_id")

# moviemat = df.pivot_table(index="user_id", columns="title", values="rating")
# ratings = pd.DataFrame(df.groupby('title').mean()['rating'])
# ratings['no_of_ratings'] = pd.DataFrame(df.groupby('title').count()['rating'])
# corr_starwars = moviemat.corrwith(moviemat['Star Wars (1977)'])
# corr_starwars = pd.DataFrame(corr_starwars, columns=['Correlation'])
# corr_starwars.dropna(inplace=True)
# corr_starwars = corr_starwars.join(ratings['no_of_ratings'])
# corr_starwars = corr_starwars[corr_starwars['no_of_ratings'] > 100].sort_values('Correlation', ascending=False)

# app = Flask(__name__, template_folder='template', static_folder='posters')

# @app.route('/')
# def home():
#     return render_template('index.html', movie_titles=movie_title['title'])

# @app.route('/recommend', methods=['POST'])
# def recommend_movies():
#     movie_name = request.form['movie_name']
#     predictions = predict_movies(movie_name)
#     return render_template('recommendations.html', movie_name=movie_name, predictions=predictions)

# def predict_movies(movie_name):
#     movie_user_ratings = moviemat[movie_name]  
#     similar_to_movie = moviemat.corrwith(movie_user_ratings)
#     corr_movie = pd.DataFrame(similar_to_movie, columns=['Correlation'])
#     corr_movie.dropna(inplace=True)
#     corr_movie = corr_movie.join(ratings['no_of_ratings'])
#     predictions = corr_movie[corr_movie['no_of_ratings'] > 100].sort_values('Correlation', ascending=False)
#     return predictions.head(1)

# if __name__ == '__main__':
#     app.run(debug=True)