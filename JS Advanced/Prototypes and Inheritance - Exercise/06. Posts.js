function solve() {
    class Post {
        constructor(title, content) {
            this.title = title;
            this.content = content;
        }
 
        toString() {
            return `Post: ${this.title}\nContent: ${this.content}`
        }
    }
 
    class SocialMediaPost extends Post{
        constructor(title, content, likes, dislikes) {
            super(title, content)
            this.likes = likes;
            this.dislikes = dislikes;
            this.comments = [];
        }
 
        addComment(str) {
            this.comments.push(str);
        }
 
        toString() {
            let result = super.toString() + `\nRating: ${this.likes - this.dislikes}`;
 
            if (this.comments.length == 0) {
                return result;
            }
 
            result += "\nComments:"
 
            this.comments.forEach((comment)=> {
                result+= `\n * ${comment}`;
            })
 
            return result;
        }
    }
 
    class BlogPost extends Post {
        constructor(title, content, views) {
            super(title, content);
            this.views = views;
        }
 
        view() {
            this.views += 1;
            return this;
        }
 
        toString() {
            return super.toString() + `\nViews: ${this.views}`;
        }
    }
 
    return {
        Post, BlogPost, SocialMediaPost
    }
}