class content:
    content_amount = 0

    # Constructor Function
    def __init__(self, t, m):
        self.text = t
        self.media = m
        self.likes = 0

        print("New content has been added")

        content.content_amount += 1

def main():
    my_posts = []

    some_content = content("My Vacation", "./vacation_pic1.jpeg")

    my_posts.append(some_content)


    some_content = content("Jumping from a plane", "./vacation_jump1.mp4")

    my_posts.append(some_content)


    print(my_posts[0].text)
    print(my_posts[0].media)

if __name__ == "__main__":
    main()