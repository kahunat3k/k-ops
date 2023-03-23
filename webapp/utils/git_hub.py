from github import Github, InputGitAuthor

# # First create a Github instance:

# # using an access token
# g = Github("<token>")

# # Then play with your Github objects:
# for repo in g.get_user().get_repos():
#     print(repo.name)

class STGithub():

    # def __init__(self, tokenaccess :str):
    def __init__(self,token:str=None):
        #TODO: Rever parametrização para receber token
        #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

        if token == None:
            self.token = '<token>'
        else:
            self.token = token

        self.git_hub = Github(login_or_token=self.token)
        self.contents = ''

    def getitemcontent(self, file:str, repo:str)->dict:

        repo = self.git_hub.get_repo(full_name_or_id=repo)

        content = repo.get_contents(path=file)

        if content:

            return content.content

    def getrepos(self) -> None:

        repos_list = ['']
        orgs_list = []


        for org in  self.git_hub.get_user().get_orgs():
            orgs_list.append(org.name)

            for repo in org.get_repos():

                repos_list.append(org.name + "/" + repo.name)

        return repos_list

    def getfile(self, prefix:str) -> None:

        content_path = f"aws/resources/aws_{prefix}.yml"

        repo = self.git_hub.get_repo('kahunat3k/k-ops')

        self.contents = repo.get_contents(path=content_path)


    def push(self,path, message, content, branch, update=False):
        # push(file_path, "Add pytest to dependencies.", data, "update-dependencies", update=True)

        repo = self.git_hub.get_repo('<organization>/<repo>')

        author = InputGitAuthor(
            "SREOps",
            "sreops@fellfree.com"
        )
        
        source = repo.get_branch("master")
        
        repo.create_git_ref(ref=f"refs/heads/{branch}", sha=source.commit.sha)  # Create new branch from master
        
        if update:  # If file already exists, update it
            contents = repo.get_contents(path, ref=branch)  # Retrieve old file to get its SHA and path
            repo.update_file(contents.path, message, content, contents.sha, branch=branch, author=author)  # Add, commit and push branch
        else:  # If file doesn't exist, create it
            repo.create_file(path, message, content, branch=branch, author=author)  # Add, commit and push branch

        


# # Init app
# if __name__ == '__main__':

#     ob = STGithub()

#     ob.getfile(prefix='s3')

#     print(bytes.decode(base64.b64decode(ob.contents.content)))
