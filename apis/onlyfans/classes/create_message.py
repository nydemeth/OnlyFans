class create_message:
    def __init__(self, option={}) -> None:
        self.responseType: str = option.get("responseType")
        self.text: str = option.get("text")
        self.lockedText: bool = option.get("lockedText")
        self.isFree: bool = option.get("isFree")
        self.price: float = option.get("price")
        self.isMediaReady: bool = option.get("isMediaReady")
        self.mediaCount: int = option.get("mediaCount")
        self.media: list = option.get("media")
        self.previews: list = option.get("previews")
        self.isTip: bool = option.get("isTip")
        self.isReportedByMe: bool = option.get("isReportedByMe")
        self.fromUser: dict = option.get("fromUser")
        self.isFromQueue: bool = option.get("isFromQueue")
        self.queueId: int = option.get("queueId")
        self.canUnsendQueue: bool = option.get("canUnsendQueue")
        self.unsendSecondsQueue: int = option.get("unsendSecondsQueue")
        self.id: int = option.get("id")
        self.isOpened: bool = option.get("isOpened")
        self.isNew: bool = option.get("isNew")
        self.createdAt: str = option.get("createdAt")
        self.changedAt: str = option.get("changedAt")
        self.cancelSeconds: int = option.get("cancelSeconds")
        self.isLiked: bool = option.get("isLiked")
        self.canPurchase: bool = option.get("canPurchase")
        self.canPurchaseReason: str = option.get("canPurchaseReason")
        self.canReport: bool = option.get("canReport")
