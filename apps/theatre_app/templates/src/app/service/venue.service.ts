import { Injectable } from "@angular/core";
import { Http } from "@angular/http";
import "rxjs";

@Injectable()
export class VenueService {
  constructor(private _http: Http) {}

  createVenue(venue) {
    return this._http
      .post("/venue", venue)
      .map(data => data.json())
      .toPromise();
  }
  getVenue(venue) {
    return this._http.get("/venue", venue).map(data => data.json()).toPromise();
  }
  updateConflict(conflict) {
    return this._http
      .patch(`/venue/${conflict._id}`, venue)
      .map(data => data.json())
      .toPromise();
  }

  destroyConflict(id: string) {
    return this._http
      .delete(`/venue/${id}`)
      .map(data => data.json())
      .toPromise();
  }
}
