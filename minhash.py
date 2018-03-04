
import random
import operator


def minhash(users, q, seed=None):
    """
    @users : [(user, [item1, item2.....), (user1, [item3, item4...])...]
    @q : the num of minhashes
    """
    random.seed(seed)
    user_minhashes = []
    for user, itemList in users:
        min_seq_items = get_min_seq_item(itemList, q)
        user_minhashes.append((user, min_seq_items))
    return user_minhashes


def get_min_seq_item(items, q):
    """
    @items : [item1, item2...]
    @q : the num of minSeq
    @return : [item7, item4, ....]
    """
    num = len(items)
    min_seqs = get_min_seq(q, num)
    return [items[i] for i in min_seqs]


def get_min_seq(q, num):
    min_seqs = []
    for i in range(q):
        seqs = [(i, random.randint(1, 10 ** 6)) for i in range(num)]
        m = min(seqs, key=operator.itemgetter(1))
        min_seqs.append(m[0])
    return min_seqs
