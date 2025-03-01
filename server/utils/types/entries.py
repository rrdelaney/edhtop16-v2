from typing import Optional
from pydantic import BaseModel


class Entry(BaseModel):
    # Temporarily, everything is optional until we clean our database.
    id: Optional[str] = None
    name: Optional[str] = None
    profile: Optional[str] = None
    decklist: Optional[str] = None
    wins: Optional[int] = None
    winsSwiss: Optional[int] = None
    winsBracket: Optional[int] = None
    winRate: Optional[float] = None
    winRateSwiss: Optional[float] = None
    winRateBracket: Optional[float] = None
    draws: Optional[int] = None
    drawsSwiss: Optional[int] = None
    losses: Optional[int] = None
    lossesSwiss: Optional[int] = None
    lossesBracket: Optional[int] = None
    standing: Optional[int] = None
    colorID: Optional[str] = None
    commander: Optional[str] = None
    tournamentName: Optional[str] = None
    TID: Optional[str] = None
    topCut: Optional[int] = None
