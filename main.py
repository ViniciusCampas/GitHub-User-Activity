#Version 1.0
#14/01/2026
#Vinicius Camparini Siqueira
import requests

def listRepoName(list1, list2=None, list3=None):
    number=1
    if list3:
        for i in range(len(list1)):
            print (f'{number} - {list1[i]} - {list2[i]} - {list3[i]}')
            number+=1
    elif list2:
        for i in range(len(list1)):
            print (f'{number} - {list1[i]} - {list2[i]}')
            number+=1
    else:
        for lis in list1:
            print(f'{number} - {lis}')
            number+=1
try:
    username=input('Digite o nome: ')

    reqst=requests.get(f'https://api.github.com/users/{username}/events')

    if reqst.status_code == 404:
        print('Usuário não encontrado!')
        exit()

    elif reqst.status_code != 200:
        print('Erro ao acessar a API do GitHub.')
        exit()

    pushEventCont=0
    pushEventRepo=[]

    issuesEventCont=0
    issuesEventRepo=[]
    issuesEventAction=[]

    watchEventCont=0
    watchEventRepo=[]

    pullRequestReviewEventCont=0
    pullRequestReviewEventRepo=[]
    pullRequestReviewEventState=[]

    createEventCont=0
    createEventRepo=[]
    createEventRefType=[]
    createEventRef=[]

    events=reqst.json()

    for event in events:
        if event['type']=='PushEvent':
            pushEventCont+=1
            pushEventRepo.append(event['repo']['name'])

        elif event['type'] == 'IssuesEvent':
            issuesEventCont+=1
            issuesEventRepo.append(event['repo']['name'])
            issuesEventAction.append(event['payload']['action'])

        elif event['type'] == 'WatchEvent'and event['payload']['action']=='started':
            watchEventCont+=1
            watchEventRepo.append(event['repo']['name'])

        elif event['type'] == 'PullRequestReviewEvent' :
            pullRequestReviewEventCont+=1
            pullRequestReviewEventRepo.append(event['repo']['name'])
            pullRequestReviewEventState.append(event['payload']['review']['state'])

        elif event['type'] == 'CreateEvent':
            createEventCont+=1
            createEventRepo.append(event['repo']['name'])
            createEventRefType.append(event['payload']['ref_type'])
            createEventRef.append(event['payload']['ref'])


    print(f'Push Event Total: {pushEventCont} ')
    listRepoName(pushEventRepo)

    print('='*50)

    print(f'Issues Event Total: {issuesEventCont} ')
    listRepoName(issuesEventRepo,issuesEventAction)

    print('='*50)

    print(f'Watch Event Total: {watchEventCont} ')
    listRepoName(watchEventRepo)

    print('='*50)

    print(f'Pull Request Review Event Total: {pullRequestReviewEventCont} ')
    listRepoName(pullRequestReviewEventRepo,pullRequestReviewEventState)

    print('='*50)

    print(f'Create Event Total: {createEventCont} ')
    listRepoName(createEventRepo,createEventRefType,createEventRef)
except requests.exceptions.RequestException:
    print('Erro de conexão com a API do GitHub.')
