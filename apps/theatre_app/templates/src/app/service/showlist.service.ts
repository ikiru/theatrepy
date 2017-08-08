import { Injectable } from "@angular/core";
import { Http } from "@angular/http";
import "rxjs";

@Injectable()
export class ShowlistService {
  constructor(private _http: Http) {}

  createShowlist(showlist) {
    return this._http
      .post("/showlist", showlist)
      .map(data => data.json())
      .toPromise();
  }
  getShowlist(showlist) {
    return this._http
      .get("/showlist", showlist)
      .map(data => data.json())
      .toPromise();
  }
  updateShowlist(showlist) {
    return this._http
      .patch(`/showlist/${showlist._id}`, showlist)
      .map(data => data.json())
      .toPromise();
  }

  destroyShowlist(id: string) {
    return this._http
      .delete(`/showlist/${id}`)
      .map(data => data.json())
      .toPromise();
  }
}
