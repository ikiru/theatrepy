import { Injectable } from "@angular/core";
import { Http } from "@angular/http";
import "rxjs";

@Injectable()
export class AuditionService {
  constructor(private _http: Http) {}

  createAudtion(audition) {
    return this._http
      .post("/audition", audition)
      .map(data => data.json())
      .toPromise();
  }
  getAudition(audition) {
    return this._http
      .get("/audition", audition)
      .map(data => data.json())
      .toPromise();
  }
  updateAudition(audition) {
    return this._http
      .patch(`/audition/${audition._id}`, audition)
      .map(data => data.json())
      .toPromise();
  }

  destroyAudition(id: string) {
    return this._http
      .delete(`/audition/${id}`)
      .map(data => data.json())
      .toPromise();
  }
}
