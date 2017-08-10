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
    return this._http.get("/venue").map(data => data.json()).toPromise();
  }
  updateVenue(venue) {
    return this._http
      .patch(`/venue/${venue._id}`, venue)
      .map(data => data.json())
      .toPromise();
  }

  destroyVenue(id: string) {
    return this._http
      .delete(`/venue/${id}`)
      .map(data => data.json())
      .toPromise();
  }
}
